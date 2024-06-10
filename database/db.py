import logging
import uuid
import aiosqlite

logger = logging.getLogger(__name__)
from data.records import records_data, images_data, categories_data


class BotDB:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None
        logger.debug("Database instance created")

    async def get_connection(self):
        if self.conn is None:
            self.conn = await aiosqlite.connect(self.db_file, isolation_level=None)
        return self.conn 


    async def create_tables(self):
        async with await aiosqlite.connect(self.db_file) as conn:
            await conn.execute("""CREATE TABLE IF NOT EXISTS data(id text, position text, category text, description text)""")
            await conn.execute("""CREATE TABLE IF NOT EXISTS links(id text, position text, img text)""")
            await conn.execute("""CREATE TABLE IF NOT EXISTS categories(category text, description text)""")   
        

    async def fill_categories_from_records_file(self):
        conn = await self.get_connection()
        for record in records_data:
            try:
                await conn.execute("BEGIN")
                images = tuple(image for image in images_data if image[0] == record[0])
                await self.insert_record(record, images)
                await conn.commit()
            except Exception as e:
                await conn.rollback()


    async def fill_data_from_records_file(self):
        for record in records_data:
            images = tuple(image for image in images_data if image[0] == record[0])
            print(f"images: {images}")
            await self.insert_record(record, images)
        
        
    async def insert_record(self, table_one_data, table_two_data):
        id = str(uuid.uuid4())
        data = (id,) + table_one_data
        conn = await self.get_connection()
        await conn.execute("INSERT INTO data VALUES(?,?,?,?)", data)
        for img in table_two_data:
            data = (id,) + img
            await conn.execute("INSERT INTO links VALUES(?,?,?)", data)
        await conn.commit()
        
    
    async def get_categories(self) -> list:
        conn = await self.get_connection()
        cursor = await conn.execute("""SELECT DISTINCT category from data""")
        rows = await cursor.fetchall()
        return rows
       

    async def get_data_by_category(self, category) -> list:
        conn = await self.get_connection()
        cursor = await conn.execute("""SELECT id, position from data WHERE category = ?""", (category,))
        rows = await cursor.fetchall()
        return rows
    

    async def get_description_by_category(self, category) -> str:
        conn = await self.get_connection()
        cursor = await conn.execute("""SELECT description from categories WHERE category = ?""", (category,))
        row = await cursor.fetchone()
        return row
    

    async def get_description_by_position(self, position) -> str:
        conn = await self.get_connection()
        cursor = await conn.execute("""SELECT description from data WHERE id = ?""", (position,))
        row = await cursor.fetchone()
        return row[0]
    
    
    async def get_position_photos(self, position) -> list:
        conn = await self.get_connection()
        cursor = await conn.execute("""SELECT img from links WHERE id = ?""", (position,))
        rows = await cursor.fetchall()
        return rows


    async def get_category_by_id(self, id) -> str:
        conn = await self.get_connection()
        cursor = await conn.execute("""SELECT category from data WHERE id = ?""", (id,))
        row = await cursor.fetchone()
        return row[0]
    