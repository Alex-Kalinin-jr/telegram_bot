import sqlite3
import logging
import uuid

logger = logging.getLogger(__name__)
from data.records import records_data, images_data

class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data(id TEXT, category TEXT, name TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS links(id TEXT, path TEXT)")
        for i in range(len(records_data)):
            id = str(uuid.uuid4())
            self.cursor.execute("INSERT INTO data VALUES(?,?,?)", (id, records_data[i][1], records_data[i][0]))
            self.cursor.execute("INSERT INTO links VALUES(?,?)", (id, images_data[i]))
        self.conn.commit()
    
    
    def make_backup(self, dst_path):
        dst = sqlite3.connect(dst_path)
        self.conn.backup(dst)
        dst.close()
        
        
    def insert_record(self, table_one_data, table_two_data):
        id = str(uuid.uuid4())
        self.cursor.execute("INSERT INTO data VALUES(?,?,?)", id, table_one_data)
        for img in table_two_data:
            self.cursor.execute("INSERT INTO links VALUES(?,?)", id, img)
        self.conn.commit()
        
    
    def get_categories(self) -> list:
        categories = self.cursor.execute("""SELECT DISTINCT category from data""").fetchall()
        logger.debug(f"Gotten categories are {categories}")
        return categories
    
    
    def get_data_by_category(self, category) -> list:
        data = self.cursor.execute("""SELECT * from data WHERE category = ?""", (category,)).fetchall()
        logger.debug(f"I am in categories --->>> Gotten data are {data}")
        return data
