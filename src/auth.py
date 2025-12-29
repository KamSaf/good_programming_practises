from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from src.config import SECRET_KEY, HASH_ALGORITHM


security = HTTPBearer()


def create_token(username: str, roles: str) -> str:
    payload = {
        "sub": username,
        "roles": roles,
        "iat": datetime.now(),
        "exp": datetime.now() + timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=HASH_ALGORITHM)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASH_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def require_admin(user=Depends(get_current_user)) -> dict:
    if "ROLE_ADMIN" not in user["roles"]:
        raise HTTPException(status_code=403, detail="Admin only")
    return user
