from aiogram import types
from fastapi import APIRouter

from config import BOT_TOKEN
from bot import dp, bot


router = APIRouter(
    prefix="/bot",
    tags=["Telegram Bot"],
)

@router.post(f"/{BOT_TOKEN}")
async def bot_webhook(update: types.Update):
    try:
        await dp.feed_update(bot=bot, update=update)
    except Exception as e:
        print("Error processing update:", e)