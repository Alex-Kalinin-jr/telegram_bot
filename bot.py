import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN, BOT_TIMEZONE, NGROK_TOKEN
from services.api_session import AsyncRequestSession
from routers.test_router import router
from database.db import BotDB


logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',

)

db_instance = BotDB('database.db')
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp['db_instance'] = db_instance
dp.include_router(router)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))