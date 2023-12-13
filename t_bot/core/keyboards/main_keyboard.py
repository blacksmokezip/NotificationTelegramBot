from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()

    kb.button(text="Добавить уведомление 🔔")
    kb.button(text="Удалить уведомление ❌")
    kb.button(text="Список уведомлений 📋")
    kb.button(text="Установить часовой пояс 🕞")

    kb.adjust(2)

    return kb.as_markup(resize_keyboard=True)
