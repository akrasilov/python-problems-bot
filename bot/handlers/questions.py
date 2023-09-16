import logging

from telegram import (
    Update,
)
from telegram import User as TGUser
from telegram.constants import ParseMode
from telegram.error import BadRequest
from telegram.ext import ContextTypes

from bot.handlers.states import States
from src.services.questions import QuestionsService
from src.services.users import User, UsersService
from src.texts import CORRECT_ANSWER_TEXT, ENOUGH_QUESTIONS_FOR_TODAY, INCORRECT_ANSWER_TEXT
from src.utils.postgres_pool import pg_pool
from src.utils.telegram.callback_data import ParsedCallbackQuestionsData, parse_callback_questions_data
from src.utils.telegram.job_queue import create_send_questions_task
from src.utils.telegram.send_message import send_message, send_question
from src.utils.formaters import format_explanation

logger = logging.getLogger(__name__)


async def _send_daily_questions_task(context: ContextTypes.DEFAULT_TYPE) -> str | None:
    users_service = UsersService(pg_pool=pg_pool)
    questions_service = QuestionsService(pg_pool=pg_pool)

    user_id = context.job.data
    user: User = await users_service.get_by_id(user_id=user_id)

    question = await questions_service.get_new_random_question_for_user(user_id=user.id)
    if question:
        await send_question(
            bot=context.bot,
            chat_id=context.job.chat_id,
            question=question,
            questions_service=questions_service,
            user_id=user.id
        )

    return States.daily_question


async def questions_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str | None:
    users_service = UsersService(pg_pool=pg_pool)
    questions_service = QuestionsService(pg_pool=pg_pool)

    query = update.callback_query
    await query.answer()
    try:
        # TODO: why errors here?
        await query.edit_message_reply_markup()
    except BadRequest as e:
        logger.error(e, exc_info=True)

    tg_user: TGUser = update.effective_user
    user: User = await users_service.get_or_create(tg_user=tg_user)

    callback_questions_data: ParsedCallbackQuestionsData = parse_callback_questions_data(callback_data=query.data)
    if callback_questions_data:
        # answer on previous question
        previous_question = await questions_service.get_by_id(question_id=callback_questions_data.question_id)
        if not previous_question:
            logger.error('No question found to answer. question_id: %d', callback_questions_data.question_id)
        else:
            is_correct = await questions_service.answer_question(
                question=previous_question,
                user_id=user.id,
                user_answer=callback_questions_data.answer
            )

            await query.edit_message_text(
                parse_mode=ParseMode.HTML,
                text=format_explanation(question=previous_question, is_correct=is_correct)
            )

    # send new question
    new_question = await questions_service.get_new_random_question_for_user(user_id=user.id)
    is_added = await create_send_questions_task(
        context=context,
        task=_send_daily_questions_task,
        chat_id=query.message.chat_id,
        user_id=user.id
    )
    if is_added:
        logger.info('User %d, added to queue', user.id)

    if not new_question:
        await send_message(message=query.message, text=ENOUGH_QUESTIONS_FOR_TODAY)
        return States.daily_question

    await send_question(
        message=query.message,
        question=new_question,
        questions_service=questions_service,
        user_id=user.id
    )
    return States.daily_question
