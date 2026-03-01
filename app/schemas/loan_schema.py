from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LoanBase(BaseModel):
    amount: float
    interest_rate: float
    duration_months: int
    status: str = "pending"

class LoanCreate(LoanBase):
    user_id: int

class LoanUpdate(BaseModel):
    status: Optional[str] = None

class LoanResponse(LoanBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True