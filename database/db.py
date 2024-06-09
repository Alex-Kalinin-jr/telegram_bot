import sqlite3
import logging
import uuid

logger = logging.getLogger(__name__)
from data.records import records_data, images_data, categories_data, position_descriptions

class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
    
    def make_backup(self, dst_path):
        dst = sqlite3.connect(dst_path)
        self.conn.backup(dst)
        dst.close()
     
     
    def fill_categories_from_records_file(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS categories (category TEXT, description TEXT)")
        self.cursor.executemany("INSERT INTO categories VALUES(?,?)", categories_data)
        self.conn.commit()
        
        
    def fill_data_from_records_file(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS position_descriptions (position TEXT, description TEXT)")
        self.cursor.executemany("INSERT INTO data VALUES(?, ?)", records_data)
        self.conn.commit()
        
        
    def insert_record(self, table_one_data, table_two_data):
        id = str(uuid.uuid4())
        self.cursor.execute("INSERT INTO data VALUES(?,?,?)", id, table_one_data)
        for img in table_two_data:
            self.cursor.execute("INSERT INTO links VALUES(?,?)", id, img)
        self.conn.commit()
        
    
    def get_categories(self) -> list:
        return self.cursor.execute("""SELECT DISTINCT category from data""").fetchall()
    
    
    def get_data_by_category(self, category) -> list:
        return self.cursor.execute("""SELECT * from data WHERE category = ?""", (category,)).fetchall()
    
    
# to be refactored
    def get_description_by_category(self, category) -> str:
        return self.cursor.execute("""SELECT description from categories WHERE category = ?""", (category,)).fetchone()
    
# to be refactored
    def get_description_by_position(self, position) -> str:
        return self.cursor.execute("""SELECT description from data WHERE position = ?""", (position,)).fetchone()
    
    
    def get_position_photos(self, position) -> list:
        return self.cursor.execute("""SELECT * from links WHERE id = ?""", (position,)).fetchall()

    def get_category_by_id(self, id) -> str:
        return self.cursor.execute("""SELECT category from data WHERE id = ?""", (id,)).fetchone()[0]