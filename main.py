import asyncio
import os
import logging
import sys

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import BOT_TOKEN, BOT_TIMEZONE
from services.api_session import AsyncRequestSession
from routers.test_router import router

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.__format__ = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"



async def start_scheduling(bot: Bot, session: AsyncRequestSession):
    logger.info("Starting scheduler")
    print("abc")
    scheduler = AsyncIOScheduler()
    # scheduler.add_job(update_profit, trigger="cron", day=1, hour=00, minute=00, second=5)
    # scheduler.add_job(update_profit, trigger="cron", day_of_week="mon", hour=00, minute=00, second=10)
    # scheduler.add_job(update_profit_day, trigger="cron", hour=00, minute=00, second=15, args=(bot,))
    # scheduler.add_job(autobackup_admin, trigger="cron", hour=00, args=(bot,))
    # scheduler.add_job(check_update, trigger="cron", hour=00, args=(bot, session,))
    # scheduler.add_job(check_mail, trigger="cron", hour=12, args=(bot, session,))
    logger.info("Scheduler started")
    scheduler.start()

async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()
    ar_session = AsyncRequestSession()
    dp.include_router(router)
    await start_scheduling(bot, ar_session)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())