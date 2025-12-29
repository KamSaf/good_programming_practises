import csv
import bcrypt
from sqlalchemy.orm import Session
from src.config import ROOT, ADMIN_USERNAME, ADMIN_PASSWORD
from src.models import Movie, Link, Rating, Tag, User


def read_csv(filename: str) -> list[list[str]]:
    path = ROOT / "db" / filename
    with open(path, "r") as read_file:
        next(read_file)
        return [row for row in csv.reader(read_file)]


def parse_movie_data(movie_data: dict) -> Movie:
    try:
        return Movie(title=movie_data["title"], genres=movie_data["genres"])
    except Exception as e:
        raise e


def parse_link_data(link_data: dict) -> Link:
    try:
        return Link(
            movie_id=link_data["movie_id"],
            imdb_id=link_data["imdb_id"],
            tmdb_id=link_data["tmdb_id"],
        )
    except Exception as e:
        raise e


def parse_rating_data(rating_data: dict) -> Rating:
    try:
        return Rating(
            user_id=rating_data["user_id"],
            movie_id=rating_data["movie_id"],
            rating=rating_data["rating"],
            timestamp=rating_data["timestamp"],
        )
    except Exception as e:
        raise e


def parse_tag_data(tag_data: dict) -> Tag:
    try:
        return Tag(
            user_id=tag_data["user_id"],
            movie_id=tag_data["movie_id"],
            tag=tag_data["tag"],
            timestamp=tag_data["timestamp"],
        )
    except Exception as e:
        raise e


def create_admin(db: Session) -> User:
    existing = db.query(User).filter(User.username == ADMIN_USERNAME).first()
    if existing:
        return existing

    hashed_pw = bcrypt.hashpw(ADMIN_PASSWORD.encode("utf-8"), bcrypt.gensalt()).decode(
        "utf-8"
    )

    admin = User(username=ADMIN_USERNAME, password_hash=hashed_pw, roles="ROLE_ADMIN")

    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin
