from pydantic import BaseModel
from typing import Optional

class AccountCreate(BaseModel):
    user_id: int
    initial_balance: Optional[float] = 0.0

class AccountResponse(BaseModel):
    id: int
    user_id: int
    balance: float
    status: str

    class Config:
        orm_mode = True