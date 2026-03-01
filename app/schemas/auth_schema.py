from pydantic import BaseModel, EmailStr, constr

class RegisterRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=6, max_length=72) 

class LoginRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=6, max_length=72)  

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"