from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    from_account: str
    to_account: str
    amount: float
    type: str

class TransactionResponse(BaseModel):
    id: str
    from_account: str
    to_account: str
    amount: float
    type: str
    created_at: datetime

    class Config:
        orm_mode = True