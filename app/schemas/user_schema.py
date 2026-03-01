from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    is_active: bool = True

class UserCreate(UserBase):
    password: constr(min_length=6, max_length=72) 
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[constr(min_length=6, max_length=72)] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True