from db.database import async_session
from db.db_data import *
from db.models import *


async def init_db_by_data():
    async with async_session() as session:
        for category in categories:
            record_cat = Categories(name=category["name"],
                                    description=category["description"])
            session.add(record_cat)
            await session.commit()

            related_positions = [x for x in positions if x["category"] == category["name"]]
            if not related_positions == []:
                for pos in related_positions:
                    record_pos = Positions(position=pos["name"], 
                                            description=pos["description"], category = record_cat)
                    session.add(record_pos)
                    await session.commit()
                    
                    related_imgs = pos["img"]
                    if not related_imgs == []:
                        for img in related_imgs:
                            record_img = Links(position = record_pos, img=img)
                            session.add(record_img)
                        await session.commit()
                        session.refresh(record_pos)
                        print(f"Created: {record_pos}")
            
