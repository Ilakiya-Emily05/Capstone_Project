from fastapi import FastAPI
from app.api.routes import accounts
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Account Service")

app.include_router(accounts.router)