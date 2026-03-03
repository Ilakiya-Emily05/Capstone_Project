from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI(title="Auth Service")

app.include_router(auth.router)