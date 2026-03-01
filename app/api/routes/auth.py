from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth_schema import RegisterRequest, LoginRequest, TokenResponse
from app.core.dependencies import get_db
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=TokenResponse)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    try:
        user = register_user(db, email=request.email, password=request.password)
        token_data = {"sub": str(user.id)}
        token = login_user(db, email=request.email, password=request.password)
        return token
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    try:
        return login_user(db, email=request.email, password=request.password)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))