import uvicorn
from src.config import engine, SessionLocal
from src.models import Base
from src.utils import create_admin

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    create_admin(SessionLocal())
    uvicorn.run("src.main:app", reload=True)
