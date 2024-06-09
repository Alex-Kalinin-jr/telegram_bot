import sqlite3
import logging
import uuid

logger = logging.getLogger(__name__)
from data.records import records_data, images_data, categories_data

class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
    
    def make_backup(self, dst_path):
        dst = sqlite3.connect(dst_path)
        self.conn.backup(dst)
        dst.close()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS data(id text, position text, category text, description text)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS links(id text, position text, img text)""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS categories(category text, description text)""")   
        

    def fill_categories_from_records_file(self):
        for category in categories_data:
            print(f"category: {category}")
            self.cursor.execute("INSERT INTO categories VALUES(?,?)", category)
        self.conn.commit()


    def fill_data_from_records_file(self):
            for record in records_data:
                images = tuple(image for image in images_data if image[0] == record[0])
                print(f"images: {images}")
                self.insert_record(record, images)
        
        
    def insert_record(self, table_one_data, table_two_data):
        id = str(uuid.uuid4())
        data = (id,) + table_one_data
        self.cursor.execute("INSERT INTO data VALUES(?,?,?,?)", data)
        for img in table_two_data:
            data = (id,) + img
            self.cursor.execute("INSERT INTO links VALUES(?,?,?)", data)
        self.conn.commit()
        
    
    def get_categories(self) -> list:
        return self.cursor.execute("""SELECT DISTINCT category from data""").fetchall()
    
    
    def get_data_by_category(self, category) -> list:
        return self.cursor.execute("""SELECT id, position from data WHERE category = ?""", (category,)).fetchall()
    
    
# to be refactored
    def get_description_by_category(self, category) -> str:
        return self.cursor.execute("""SELECT description from categories WHERE category = ?""", (category,)).fetchone()
    
# to be refactored
    def get_description_by_position(self, position) -> str:
        return self.cursor.execute("""SELECT description from data WHERE id = ?""", (position,)).fetchone()
    
    
    def get_position_photos(self, position) -> list:
        return self.cursor.execute("""SELECT * from links WHERE id = ?""", (position,)).fetchall()

    def get_category_by_id(self, id) -> str:
        return self.cursor.execute("""SELECT category from data WHERE id = ?""", (id,)).fetchone()[0]