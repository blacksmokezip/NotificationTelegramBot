import asyncio

from aiogram import Router, F
from aiogram.types import Message

from datetime import datetime

from core.hash import create_hash


router = Router()


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
        message: Message,
        notifications: dict
):
    date = message.text[-17:]
    name = message.text[:-18]
    hash = create_hash(name)
    try:
        wait = datetime.strptime(
            date,
            "%d/%m/%y %H:%M:%S"
        ) - datetime.now()
        delay = int(wait.total_seconds())
        notifications[hash] = [name, date]
        await message.answer(
            "Уведомление успешно добавлено!"
        )
        await asyncio.sleep(delay)
        if notifications.get(hash) is None:
            return
        else:
            await message.answer(notifications[hash][0])
            notifications.pop(hash)
    except ValueError:
        await message.answer(
            "Неверный формат уведомления!" +
            " Попробуйте ещё раз"
        )
