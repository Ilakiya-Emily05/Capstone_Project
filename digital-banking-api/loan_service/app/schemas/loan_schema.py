from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class LoanStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class LoanCreate(BaseModel):
    user_id: str
    amount: float
    interest_rate: float = 10.0

class LoanResponse(BaseModel):
    id: str
    user_id: str
    amount: float
    interest_rate: float
    status: LoanStatus
    created_at: datetime

    class Config:
        orm_mode = True