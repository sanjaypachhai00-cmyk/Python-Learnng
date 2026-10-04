import sqlite3


def connect_db():
    return sqlite3.connect("users.db")


def create_table():
    db = connect_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            skill TEXT
        )
    """)

    db.commit()
    db.close()