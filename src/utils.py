import os.path
import sqlite3

FILE_PATH = "queue.db"


def connect() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect(FILE_PATH)
    return (conn, conn.cursor())


def create_database() -> None:
    if os.path.isfile(FILE_PATH):
        return
    conn, cur = connect()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS task
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT,
            status TEXT
        )
        """
    )
    conn.commit()
    print("\n✅ Database file created!")
    conn.close()


if __name__ == "__main__":
    pass
