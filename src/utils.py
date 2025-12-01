import csv
from src.config import ROOT
from src.models import Movie, Link, Rating, Tag


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
