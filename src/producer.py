from pathlib import Path

FILE_PATH = "queue.txt"
DEFAULT_TASK_NAME = "do something"


def create_task(task_name: str = DEFAULT_TASK_NAME) -> None:
    Path(FILE_PATH).touch(exist_ok=True)
    with open(FILE_PATH, "r+") as file:
        task_num = sum(1 for _ in file) + 1
        file.write(f"{task_num} | {task_name} | pending\n")


if __name__ == "__main__":
    create_task()
