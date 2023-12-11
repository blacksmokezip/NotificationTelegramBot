from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import psycopg2
import os
from dotenv import load_dotenv, find_dotenv

from bot.core.keyboards.timezone_keyboard import get_kb
from bot.core.tools.constants import TIMEZONES
from bot.core.tools.database import update_timezone


router = Router()
load_dotenv(find_dotenv())


@router.message(F.text.lower() == "установить часовой пояс 🕞")
async def set_timezone(message: Message):
    await message.answer(
        "Выбери свой часовой пояс:",
        reply_markup=get_kb()
    )


@router.callback_query(F.data)
async def callback_timezone(callback: CallbackQuery):
    action = callback.data
    conn = psycopg2.connect(
        os.environ.get(
            "DATABASE_URL"
        )
    )
    try:
        update_timezone(
            conn,
            int(callback.from_user.id),
            TIMEZONES[action]
        )
        await callback.answer(
            "Часовой пояс успешно изменён!"
        )
    except Exception:
        await callback.answer(
            "Произошла ошибка на сервере..."
        )
