import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN, REDIS_URL
from routers.test_router import router
from database.db import BotDB
from aiogram.fsm.storage.redis import RedisStorage, Redis
from routers.admin_router import r_admin




logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',

)


db_instance = BotDB('database.db')
# storage = MemoryStorage()
redis = Redis(host=REDIS_URL)
storage = RedisStorage(redis=redis)

dp = Dispatcher(storage=storage)
dp['db_instance'] = db_instance
dp.include_router(r_admin)
dp.include_router(router)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
