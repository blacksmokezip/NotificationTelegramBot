from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text="Калининград", callback_data="Калининград")
    kb.button(text="Магадан", callback_data="Магадан")
    kb.button(text="Якутск", callback_data="Якутск")
    kb.button(text="Владивосток", callback_data="Владивосток")
    kb.button(text="Иркутск", callback_data="Иркутск")
    kb.button(text="Красноярск", callback_data="Красноярск")
    kb.button(text="Омск", callback_data="Омск")
    kb.button(text="Екатеринбург", callback_data="Екатеринбург")
    kb.button(text="Москва", callback_data="Москва")
    kb.button(text="Самара", callback_data="Самара")
    kb.button(text="Камчатка", callback_data="Камчатка")

    kb.adjust(2)

    return kb.as_markup()
