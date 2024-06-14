import asyncio
from utils.utils import init_db_by_data


if __name__ == "__main__":
    asyncio.run(init_db_by_data())