import bcrypt
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from src.config import get_db
from src.auth import create_token, get_current_user, require_admin
from src.models import User

router = APIRouter(prefix="/auth")


@router.post("/login", status_code=200)
def login(data: dict = Body(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data["username"]).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not bcrypt.checkpw(data["password"].encode(), str(user.password_hash).encode()):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(str(user.username), user.roles)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/users", status_code=201)
def create_user(
    data: dict = Body(...),
    db: Session = Depends(get_db),
    _: dict = Depends(require_admin),
):
    hashed_pw = bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())
    user = User(
        username=data["username"], password_hash=hashed_pw.decode(), roles=data["roles"]
    )
    db.add(user)
    db.commit()
    return {"message": "User created"}


@router.get("/user_details", status_code=200)
def user_details(user=Depends(get_current_user)):
    return user
