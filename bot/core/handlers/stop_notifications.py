from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from core.keyboards.main_keyboard import get_kb


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! " +
        "Я буду напоминать тебе о важных событиях. " +
        "Просто нажми кнопку 'добавить уведомление'",
        reply_markup=get_kb()
    )


@router.message(F.text.lower() == "удалить уведомление ❌")
async def stop_notification(
        message: Message,
        notifications: dict
):
    items = list(notifications.items())
    if not items:
        await message.answer(
            "Список пуст"
        )
    else:
        reply = "\n".join(
            [f"{i[0]}: {i[1][0]} {i[1][1]}" for i in items]
        )
        await message.answer(
            reply
        )
        await message.answer(
            "Введи id уведомления, которое нужно удалить"
        )


@router.message(lambda message: message.text.isdigit())
async def stop(
        message: Message,
        notifications: dict
):
    try:
        id = int(message.text)
        notifications.pop(id)
        await message.answer(
            "Уведомлние успешно удалено!"
        )
    except KeyError:
        await message.answer(
            "Неверный id уведомления, попробуйте ещё раз"
        )
