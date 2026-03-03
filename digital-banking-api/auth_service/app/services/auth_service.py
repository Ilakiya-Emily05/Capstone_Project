from sqlalchemy.orm import Session
from app.models.user import User
from app.repositories.user_repository import get_user_by_email, create_user
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, email: str, password: str):
    existing_user = get_user_by_email(db, email)
    if existing_user:
        raise ValueError("User already exists")
    user = User(email=email, hashed_password=hash_password(password))
    return create_user(db, user)

def login_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    token = create_access_token({"sub": user.email, "role": user.role})
    return token