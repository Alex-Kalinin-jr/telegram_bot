import argparse

import sqlite3


parser = argparse.ArgumentParser(
    prog="dbhandler",
    description='this script helps fill and check database data',
    epilog='abc'
)


conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
rows = cursor.fetchall()
print(rows)


cursor.execute("SELECT * FROM links")
print("####################LINK COLUMNS ARE:")
print(cursor.description)
print("####################LINK ROWS ARE:")
rows = cursor.fetchall()
for row in rows:
    print(row)


cursor.execute("SELECT * FROM data")
print("####################DATA COLUMNS ARE:")
print(cursor.description)
rows = cursor.fetchall()
print("####################DATA ROWS ARE:")
for row in rows:
    print(row)


cursor.execute("SELECT * FROM categories")
print("####################CATEGORIES COLUMNS ARE:")
print(cursor.description)
rows = cursor.fetchall()
print("####################CATEGORIES ROWS ARE:")
for row in rows:
    print(row)