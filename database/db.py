import sqlite3
import logging
import uuid

logger = logging.getLogger(__name__)
from data.records import records_data, images_data

class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
    
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
        return self.cursor.execute("""SELECT DISTINCT category from data""").fetchall()
    
    
    def get_data_by_category(self, category) -> list:
        return self.cursor.execute("""SELECT * from data WHERE category = ?""", (category,)).fetchall()
