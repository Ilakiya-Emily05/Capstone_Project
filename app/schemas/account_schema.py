from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AccountBase(BaseModel):
    account_type: str
    balance: float = 0.0
    is_active: bool = True

class AccountCreate(AccountBase):
    user_id: int

class AccountUpdate(BaseModel):
    balance: Optional[float] = None
    is_active: Optional[bool] = None

class AccountResponse(AccountBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True