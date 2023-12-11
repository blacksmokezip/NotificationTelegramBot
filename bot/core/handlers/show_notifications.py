from aiogram import Router, F
from aiogram.types import Message
import os
import psycopg2
from dotenv import load_dotenv, find_dotenv

from bot.core.tools.database import select


router = Router()
load_dotenv(find_dotenv())
url = os.environ.get("DATABASE_URL")


@router.message(F.text.lower() == "список уведомлений 📋")
async def show_list(
        message: Message
):
    conn = psycopg2.connect(url)
    items = select(
        conn,
        "notifications",
        "user_id",
        int(message.from_user.id)
    )
    if not items:
        await message.answer(
            "Список пуст"
        )
    else:
        reply = "\n".join(
            [f"{i[2]}: {i[3]} {i[4]}" for i in items]
        )
        await message.answer(
            "Список уведомлений:\n" + reply
        )
