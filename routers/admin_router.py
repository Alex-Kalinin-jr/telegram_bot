import logging

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from middlewares.admin_middleware import AdmMiddleware

logger = logging.getLogger(__name__)
admin_router = Router()
admin_router.message.outer_middleware(AdmMiddleware())
admin_router.callback_query.outer_middleware(AdmMiddleware())

@admin_router.message(Command(commands=['admin']))
async def command_admin(message: Message):
    await message.answer('Admin panel')