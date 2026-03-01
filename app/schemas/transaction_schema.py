from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float
    transaction_type: str   
    description: Optional[str] = None

class TransactionCreate(TransactionBase):
    account_id: int

class TransactionResponse(TransactionBase):
    id: int
    account_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class TransferRequest(BaseModel):
    sender_account_id: int
    receiver_account_id: int
    amount: float
    currency: Optional[str] = "USD"