from typing import Any, Awaitable, Callable, Dict
import logging
import inspect
from pprint import pprint
import time

from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject
from aiogram.dispatcher.flags import get_flag


logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):

    async def __call__(
            self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        data["time_start"] = time.clock_gettime(time.CLOCK_MONOTONIC)
        data["func_name"] = "mock_function"
        return await handler(event, data)
    
class LoggingInnerMiddleware(BaseMiddleware):
    async def __call__(
            self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        data["time_start"] = time.clock_gettime(time.CLOCK_MONOTONIC)
        result = await handler(event, data)
        tt = get_flag(data, "f_name")
        logger.debug(f"{tt}: {time.clock_gettime(time.CLOCK_MONOTONIC) - data['time_start']}")
        return result