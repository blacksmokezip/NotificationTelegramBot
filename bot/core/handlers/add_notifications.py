import asyncio
import psycopg2
import os
import pytz
from dotenv import load_dotenv, find_dotenv
from aiogram import Router, F
from aiogram.types import Message
from datetime import datetime

from core.tools.hash import create_hash
from core.tools.database import (
    add_a_notification,
    select,
    delete_notification
)


router = Router()
load_dotenv(find_dotenv())


@router.message(F.text.lower() == "добавить уведомление 🔔")
async def add_notification(message: Message):
    await message.answer(
        "Напиши, о чём тебе напомнить в формате:\n" +
        "<Название уведомления> <ДД/ММ/ГГ чч:мм:сс>\n" +
        "Без '<>' и ОБЯЗАТЕЛЬНО с пробелом между датой и названием"
    )
    await message.answer(
        "Пример:\n" +
        "Покормить кота 15/11/26 12:00:00"
    )


@router.message(F.text)
async def add(
        message: Message
):
    date = message.text[-17:]
    name = message.text[:-18]
    hash = create_hash(name)
    conn = psycopg2.connect(
        os.environ.get(
            "DATABASE_URL"
        )
    )
    user = select(
        conn,
        "users",
        "user_id",
        int(message.from_user.id)
    )[0]
    try:
        input_datetime = pytz.timezone(user[3]).localize(
            datetime.strptime(date, "%d/%m/%y %H:%M:%S")
        )
        current_datetime = datetime.now(
            pytz.timezone(user[3])
        )
        wait = input_datetime - current_datetime
        delay = int(wait.total_seconds())
        add_a_notification(
            conn,
            int(message.from_user.id),
            hash,
            name,
            date
        )
        await message.answer(
            "Уведомление успешно добавлено!"
        )
        await asyncio.sleep(delay)
        n = select(
            conn,
            "notifications",
            "hash",
            hash
        )
        if not n:
            return
        else:
            await message.answer(
                f"{n[0][3]} {n[0][4]}"
            )
            delete_notification(
                conn,
                hash
            )
    except ValueError:
        await message.answer(
            "Неверный формат уведомления!" +
            " Попробуйте ещё раз"
        )
