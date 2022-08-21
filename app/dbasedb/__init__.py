import sqlite3

def get_db():
    conn = sqlite3.connect('app/database.db')
    return conn