import uvicorn
from src.config import engine
from src.models import Base

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    uvicorn.run("src.main:app", reload=True)
