from pathlib import Path
from sqlalchemy import create_engine

ROOT = Path(__file__).parent.parent
engine = create_engine("sqlite:///database.db", echo=True)
