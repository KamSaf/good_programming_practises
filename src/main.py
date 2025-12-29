from fastapi import FastAPI
from src.routes.movies import router as rm
from src.routes.links import router as rl
from src.routes.ratings import router as rr
from src.routes.tags import router as rt
from src.routes.users import router as ru


app = FastAPI()

for router in (rm, rl, rr, rt, ru):
    app.include_router(router)


@app.get("/")
def root() -> dict:
    return {"hello": "world"}
