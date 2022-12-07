import os
import sqlite3
from pathlib import Path

DB_PATH = "users.db"

def query_db(query, args=(), one=False, commit=False):
    with sqlite3.connect(DB_PATH) as conn:
        conn.set_trace_callback(print)
        cur = conn.cursor().execute(query, args)
        if commit:
            conn.commit()
        return cur.fetchone() if one else cur.fetchall()