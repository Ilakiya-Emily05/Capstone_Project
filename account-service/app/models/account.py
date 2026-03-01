from sqlalchemy import Column, Integer, String, Float, Boolean
from app.core.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, unique=True)
    balance = Column(Float, default=0.0)
    status = Column(String, default="ACTIVE")  # ACTIVE, FROZEN