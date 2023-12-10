from aiogram import Router, F
from aiogram.types import Message
import os
import psycopg2
from dotenv import load_dotenv, find_dotenv

from core.tools.database import (
    select_notifications,
    delete_notification
)


router = Router()
load_dotenv(find_dotenv())
url = os.environ.get("DATABASE_URL")


@router.message(F.text.lower() == "удалить уведомление ❌")
async def stop_notification(
        message: Message
):
    conn = psycopg2.connect(url)
    items = select_notifications(
        conn,
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
            reply
        )
        await message.answer(
            "Введи id уведомления, которое нужно удалить"
        )


@router.message(lambda message: message.text.isdigit())
async def stop(
        message: Message
):
    try:
        conn = psycopg2.connect(url)
        id = int(message.text)
        delete_notification(conn, id)
        await message.answer(
            "Уведомлние успешно удалено!"
        )
    except KeyError:
        await message.answer(
            "Неверный id уведомления, попробуйте ещё раз"
        )
