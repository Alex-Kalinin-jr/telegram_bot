from db.database import async_session
from db.db_data import *
from db.models import *


async def init_db_by_data():
    async with async_session() as session:
        pass

