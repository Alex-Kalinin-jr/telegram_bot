import asyncio
import os
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN, BOT_TIMEZONE
from services.api_session import AsyncRequestSession
from routers.test_router import router
from database.db import BotDB

logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',

)


async def main():
    db_instance = BotDB('database.db')
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp['db_instance'] = db_instance
    dp.include_router(router)
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())