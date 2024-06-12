from typing import Any, Awaitable, Callable, Dict
import logging
import inspect
from pprint import pprint
import time

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject
from aiogram.dispatcher.flags import get_flag, extract_flags


logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s - %(message)s')
handler = logging.FileHandler('functions_time.log')
handler.setFormatter(formatter)
logger.addHandler(handler)


async def handle_outer_middleware(handler, event, data):
    data["time_start"] = time.clock_gettime(time.CLOCK_MONOTONIC)
    return await handler(event, data)
    

async def logging_middleware(handler, event, data):
    flags_data = extract_flags(data)
    timedelta = time.clock_gettime(time.CLOCK_MONOTONIC) - data["time_start"]
    logger.debug(f"{flags_data['name']} : {timedelta}")
    return await handler(event, data)