import sqlite3
DATABASE_NAME = "games.db"


def get_db():
    conn = sqlite3.connect('app/database.db')
    return conn