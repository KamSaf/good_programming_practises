from typing import Sequence
from sqlalchemy.orm import Session
from src.config import engine
from src.models import Rating
from sqlalchemy import select
from src.utils import read_csv


def load_ratings(filename: str = "ratings.csv"):
    with Session(engine) as session:
        ratings = [
            Rating(
                user_id=int(user_id),
                movie_id=int(movie_id),
                rating=float(rating),
                timestamp=int(timestamp),
            )
            for [user_id, movie_id, rating, timestamp] in read_csv(filename)
        ]
        session.add_all(ratings)
        session.commit()


def get_all_ratings() -> Sequence[Rating]:
    stmt = select(Rating)
    with Session(engine) as session:
        result = session.scalars(stmt)
        return result.all()
