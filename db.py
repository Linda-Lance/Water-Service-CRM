import sqlite3

conn = sqlite3.connect("water_service.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(customers)")
print(cursor.fetchall())

conn.close()