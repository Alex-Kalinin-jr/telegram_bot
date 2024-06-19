import asyncio
import argparse

from utils.utils import init_db_by_data
from db.database import async_session


async def main():
    await init_db_by_data(async_session())


if __name__ == "__main__":
    asyncio.run(main())