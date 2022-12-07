import os
import sqlite3
from pathlib import Path
import sentry_sdk

from flask import Flask

DB_PATH = "users.db"

def create_app():
    # init Sentry
    sentry_sdk.init(
        dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
        traces_sample_rate=1.0,
    )

    app = Flask(__name__)

    db_path = Path(DB_PATH)

    if db_path.exists():
        db_path.unlink()

    conn = sqlite3.connect(DB_PATH)
    create_table_query = """
        CREATE TABLE IF NOT EXISTS user 
        (
            id INTEGER IDENTITY PRIMARY KEY, 
            firstname TEXT,
            lastname TEXT, 
            location TEXT, 
            age INTEGER 
        )
    """
    conn.execute(create_table_query)

    insert_admin_query = """
        INSERT INTO user (id, firstname, lastname, location, age)
        VALUES (1, 'admin', 'admin', 'Toronto', 1)
    """
    conn.execute(insert_admin_query)
    conn.commit()
    conn.close()

    with app.app_context():
        from . import users
        app.register_blueprint(users.bp)
        return app