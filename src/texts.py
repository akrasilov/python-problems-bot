GREETING_TEXT: str = (
    r"""
Привет\! Я — Пит, твой карманный помощник в изучении Python и подготовке к собеседованиям\.

🔹 Выбирай уровень сложности вопросов — от новичка до опытного разработчика

🔹 Бот каждый день будет присылать 3 вопроса\. Это займет всего 5\-10 минут в день\!

🔹 Зарабатывай достижения и соревнуйся с другими пользователями
    """
)

START_BUTTON_TEXT: str = (
    'Поехали 🚀'
)

CORRECT_ANSWERS: list = [
    r"Ура, это правильный ответ\! 🎉",
    r"Точно в яблочко\! 🎯",
    r"Абсолютно верно\! 🌟",
    r"Верно\! Ты просто космос\! 🚀",
    r"Правильный ответ\! 👍",
    r"Так точно\! Ты справился на ура\! 🏆",
    r"И это правильный ответ\! ✅",
    r"Верно\! У тебя отлично получается\! 😉",
    r"Да, это правильный ответ\! 👌",
    r"Браво\! Совершенно верно\! 🤝"
]

INCORRECT_ANSWERS = [
    r"Ой\-ой, кажется, это не тот ответ 😯",
    r"Упс, мимо\! 🙊",
    "Ошибочка вышла 🙈",
    r"Не угадал\! 🙅‍♂️",
    "К сожалению, это не так 🚫",
    "Не тот ответ, друг 🕵️‍♂️"
]

ENOUGH_QUESTIONS_FOR_TODAY_TEXTS: list[str] = [
    r"""
Сегодня – всё\!

Жди новых заданий на пути к изучению Python уже завтра⚡️

Ты можешь дальше\-больше\!
Камон, эврибади пучехензап 💥
    """,
    r"""
«Для средульки хватит\!»

Новые задачки уже завтра⚡️
    """,
    r"""
На сегодня всё\!

Задачи ждут тебя завтра, а пока отдыхай и набирайся сил 🔋
    """,
    r"""
Белиссимо 🤌

Завтра жди новые крутые задачи\!
    """,
    r"""
Ты молодец🌟

Завтра встречаемся как обычно\!
    """,
    r"""
Сегодня все\!

С нетерпением жду тебя завтра👋
    """,
    r"""
На сегодня все, отдыхай\!

А я уже готовлю для тебя новые задачи на завтра 🤩
    """
]

PREPAYMENT_TEXT: str = (
    r"""
*Твой бесплатный период закончился 🙄*

Мы готовы выделить тебя из тысяч других кандидатов\!

– подготовили более 1000 вопросов с нюансами Python
– разбор более 100 типовых задачек, которые просят закодить на собеседовании
– статьи с разбором инженерных вопросов про сети и операционные системы

*Оплати следующие 30 дней тренажера\.* Для тебя это будет стоить 799 рублей\!
    """
)


THANK_YOU_FOR_PAYMENT_TEXT: str = (
    r"""
Спасибо за оплату\! Отправляемся в путешествие 💫

Если у тебя возникли какие\-либо проблемы с ботом — [пиши](http://t.me/MarksAngeles)\. Я постараюсь помочь тебе\!
    """
)

CHOOSE_LEVEL_TEXT: str = (
    r"""
👶 \- Я новичок, прошел переменные, циклы и условия в Python
👨‍🎓 \- Я уже много знаю, хочу задачи на глубину языка Python
🧑‍💻 \- Я хочу узнать больше про возможности python

Ты всегда сможешь изменить эту настройку командой: /level
    """
)

CHOOSE_LEVEL_ONBOARDING_TEXT: str = (
    rf"""
Мне уже не терпится отправить тебе задачи\!
Но для начала я хотел бы узнать твой уровень знаний, чтобы мы работали эффективно🔋
{CHOOSE_LEVEL_TEXT}
    """
)


FINISH_ONBOARDING_TEXT: str = (
    r"""
Отлично\!
С этого момента бот будет отправлять тебе вопросы, качай свои навыки в python\! Соревнуйся с другими участниками\!

А еще, вступай в [мой канал](https://t.me/python_dev_mentor)\! Там я разбираю разные интересные темы,
 помогаю готовиться к собеседованиям, да и просто со мной можно пообщаться 🙂\!
    """
)

NO_MORE_QUESTIONS_TEXT: str = (
    """
Вопросы закончились 🥲
Переключи уровень командой /level, там еще куча вопросов 🚀
Или посмотри все вопросы еще раз и подтяните свои слабые темы 😉
    """
)
