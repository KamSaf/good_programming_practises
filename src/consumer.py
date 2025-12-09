import asyncio
import os
from utils import create_database, connect, FILE_PATH

pending_tasks = []


async def check_tasks() -> None:
    global pending_tasks
    while True:
        await asyncio.sleep(5)
        conn, cur = connect()
        rows = list(cur.execute("SELECT id FROM task WHERE status = 'pending'"))
        pending_tasks_ids = [row[0] for row in rows if row[0] not in pending_tasks]
        if len(pending_tasks_ids) > 0:
            print("New tasks found!")
            pending_tasks += pending_tasks_ids
        conn.close()


def update_task_status(task_id: int, status: str) -> None:
    conn, cur = connect()
    cur.execute(
        "UPDATE task SET status = :status WHERE id = :id",
        {"status": status, "id": task_id},
    )
    conn.commit()
    conn.close()


async def consume_task() -> None:
    global pending_tasks
    while True:
        if len(pending_tasks) == 0:
            await asyncio.sleep(2)
            continue
        task_id = pending_tasks[0]
        print("Processing task...")
        pending_tasks = pending_tasks[1:]
        update_task_status(task_id=task_id, status="in_progress")
        await asyncio.sleep(30)
        update_task_status(task_id=task_id, status="done")
        print("Task done!")


async def main() -> None:
    try:
        if not os.path.isfile(FILE_PATH):
            create_database()
        print("Running...")
        await asyncio.gather(check_tasks(), consume_task())
    except asyncio.CancelledError:
        print("\nScript stopped")


if __name__ == "__main__":
    asyncio.run(main())
