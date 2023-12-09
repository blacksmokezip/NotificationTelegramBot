from aiogram import Router, F
from aiogram.types import Message


router = Router()


@router.message(F.text.lower() == "список уведомлений 📋")
async def show_list(
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
            "Список уведомлений:\n" + reply
        )
