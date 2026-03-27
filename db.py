import sqlite3

DB = "water_service.db"

def get_connection():
    return sqlite3.connect(DB)  