import sqlite3
import logging

logger = logging.getLogger(__name__)

class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data(name TEXT, category TEXT, data TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS links(name TEXT, path TEXT)")
        self.cursor.execute("""INSERT INTO data(name, category, data) VALUES('a', 'b', 'c'), ('d', 'b', 'e')""")
        res = self.cursor.execute("SELECT * FROM data")
        self.cursor.execute("""INSERT INTO links(name, path) VALUES
                ('position 1', 'abache_1.jpeg'), ('position 2', 'abache_2.jpeg')""")
        self.conn.commit()
        logger.debug(f"selection result is {res}")
    
    def get_data_by_category(self, category: str) -> list:
        return self.cursor.execute(f"SELECT * FROM data WHERE category = '{category}'").fetchall()
    
    def get_all_data(self) -> list:
        return self.cursor.execute("SELECT * FROM data").fetchall()
    
    def get_all_links(self) -> list:
        return self.cursor.execute("SELECT * FROM links").fetchall()
