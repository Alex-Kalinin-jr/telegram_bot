import asyncio
from utils.utils import init_db_by_data


async def main():
    await init_db_by_data()


if __name__ == "__main__":
    asyncio.run(main())