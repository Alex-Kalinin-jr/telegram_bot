from db.database import async_session
from db.db_data import *
from db.models import *
from sqlmodel.ext.asyncio.session import AsyncSession
            
async def init_db_by_data(session: AsyncSession):  # Pass session as argument
    for category_data in categories:
        category = Categories(name=category_data["name"], description=category_data["description"])
        session.add(category)  # Add the category first

        related_positions = [x for x in positions if x["category"] == category_data["name"]]
        for pos_data in related_positions:
            position = Positions(position=pos_data["name"], description=pos_data["description"], category=category)  # Assign category directly
            session.add(position)

            for img in pos_data["img"]:
                link = Links(position=position, img=img)
                session.add(link)

    await session.commit()