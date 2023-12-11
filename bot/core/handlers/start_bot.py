from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv, find_dotenv
import os

from core.keyboards.main_keyboard import get_kb
from core.tools.database import (
    get_connection,
    add_user,
    select
)


load_dotenv(find_dotenv())


DATABASE = os.environ.get("DATABASE_URL")
router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    conn = get_connection(DATABASE)
    user = select(
        conn,
        "users",
        "user_id",
        int(message.from_user.id)
    )
    if not user:
        add_user(
            conn,
            int(message.from_user.id),
            message.from_user.username
        )
    await message.answer(
        f"Привет, {message.from_user.first_name}! " +
        "Я буду напоминать тебе о важных событиях. " +
        "Просто нажми кнопку 'добавить уведомление'",
        reply_markup=get_kb()
    )
