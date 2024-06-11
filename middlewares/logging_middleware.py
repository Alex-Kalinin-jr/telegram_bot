from typing import Any, Awaitable, Callable, Dict
import logging
import inspect
from pprint import pprint

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseMiddleware):
    async def __call__(
            self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        result = await handler(event, data)
        # info = inspect.getmembers(handler)
        pprint(inspect.getmembers(data.get('handler')), indent=4)
        # pprint(info, indent=4)
        logger.debug(f"########THIS IS MOCK LOGGER: ")
        return result