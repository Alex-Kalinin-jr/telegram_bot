import logging
import time

from aiogram.dispatcher.flags import extract_flags


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
    logger.debug(f"user_id: {event.from_user.id}, username: {event.from_user.username}, \
user full name: {event.from_user.first_name} {event.from_user.last_name} ### {flags_data['name']} : {timedelta}")
    return await handler(event, data)
