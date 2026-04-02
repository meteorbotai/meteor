import sqlite3

from constants import DATA_DIR, DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at  INTEGER NOT NULL,
    updated_at  INTEGER NOT NULL,
    title       TEXT NOT NULL,
    status      TEXT NOT NULL DEFAULT 'pending',
    description TEXT,
    outcome     TEXT
);
CREATE TABLE IF NOT EXISTS memories (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at INTEGER NOT NULL,
    content    TEXT NOT NULL
);
"""

DATA_DIR.mkdir(parents=True, exist_ok=True)

sqlite3.connect(DB_PATH).executescript(SCHEMA)
print("DB ready.")
