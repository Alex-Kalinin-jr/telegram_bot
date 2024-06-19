import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, DB_SERVICE_URL
from routers.test_router import router
from aiogram.fsm.storage.redis import RedisStorage
from routers.admin_router import r_admin
from services.db import Interactor


logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',

)

storage = RedisStorage.from_url('redis://redis_service:6379/0')

db_service = Interactor(DB_SERVICE_URL)
dp = Dispatcher(storage=storage)
dp['db_service'] = db_service
dp.include_router(r_admin)
dp.include_router(router)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
