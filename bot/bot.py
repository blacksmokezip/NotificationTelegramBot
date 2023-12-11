import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
import os

from bot.core.handlers import (
    start_bot,
    stop_notifications,
    show_notifications,
    add_notifications,
    set_timezone
)
from bot.background import keep_alive


load_dotenv(find_dotenv())


async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    dp = Dispatcher()

    dp.include_routers(
        start_bot.router,
        set_timezone.router,
        stop_notifications.router,
        show_notifications.router,
        add_notifications.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    keep_alive()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
