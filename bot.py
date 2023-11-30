import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers


async def main() -> None:
    """Main function"""

    # load config_data
    config: Config = load_config()

    # initialize Bot and Dispatcher
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Register handlers
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # run
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
