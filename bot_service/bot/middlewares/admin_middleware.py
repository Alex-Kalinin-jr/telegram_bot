from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from utils.utils import get_admins


ADMINS = get_admins()

class AdmMiddleware(BaseMiddleware):
    async def __call__(
            self, handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        if event.from_user.id in ADMINS:
            return await handler(event, data)
        else:
            return