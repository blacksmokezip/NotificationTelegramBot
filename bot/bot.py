import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
import os

from core.handlers import stop_notifications, show_notifications, add_notifications


load_dotenv(find_dotenv())


async def main():
    bot = Bot(token=os.environ.get("TOKEN"))
    dp = Dispatcher()

    dp.include_routers(
        stop_notifications.router,
        show_notifications.router,
        add_notifications.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, notifications={})


if __name__ == "__main__":
    asyncio.run(main())
