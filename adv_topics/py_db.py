#SQLite
import sqlite3

conn = sqlite3.connect("app.db")
conn.row_factory = sqlite3.Row          # dict-like rows
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL
    )
""")

cur.execute("INSERT INTO users (email, name) VALUES (?, ?)",
            ("a@x.com", "Alice"))
conn.commit()

cur.execute("SELECT * FROM users WHERE email = ?", ("a@x.com",))
row = cur.fetchone()
print(dict(row))   # {'id': 1, 'email': 'a@x.com', 'name': 'Alice'}

conn.close()


#Context Manager
from contextlib import contextmanager

@contextmanager
def db(path="app.db"):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

with db() as conn:
    conn.execute("INSERT INTO users (email, name) VALUES (?, ?)", ("b@x.com", "Bob"))