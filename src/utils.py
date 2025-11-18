import csv
from pathlib import Path

ROOT = Path(__file__).parent.parent


def read_csv(filename: str) -> list[list[str]]:
    path = ROOT / "db" / filename
    with open(path, "r") as read_file:
        next(read_file)
        return [row for row in csv.reader(read_file)]
