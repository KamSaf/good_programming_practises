from src.config import engine
from src.models import Base
from src.queries.movies import load_movies
from src.queries.links import load_links
from src.queries.ratings import load_ratings
from src.queries.tags import load_tags


try:
    Base.metadata.create_all(engine)
    load_movies()
    load_links()
    load_ratings()
    load_tags()
    print("Data successfully loaded.")
except Exception as e:
    print(f"Error occured while trying to load data to database.\n\n{e}")
