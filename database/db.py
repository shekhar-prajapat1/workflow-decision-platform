
import sqlite3
import json

def init_db():
    conn = sqlite3.connect("audit.db")
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS audit (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        request TEXT,
        decision TEXT
    )
    ''')

    conn.commit()
    conn.close()


def insert_audit(log):

    conn = sqlite3.connect("audit.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO audit (timestamp, request, decision) VALUES (?, ?, ?)",
        (
            log["timestamp"],
            json.dumps(log["request"]),
            json.dumps(log["decision"])
        )
    )

    conn.commit()
    conn.close()
