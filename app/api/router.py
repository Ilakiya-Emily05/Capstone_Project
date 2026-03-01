from fastapi import APIRouter
from .routes import auth, accounts, transactions

api_router = APIRouter()
api_router.include_router(auth.router)
api_router.include_router(accounts.router)
api_router.include_router(transactions.router)