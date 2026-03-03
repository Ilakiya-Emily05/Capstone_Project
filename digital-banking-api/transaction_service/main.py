from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import transactions

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Transaction Service")
app.include_router(transactions.router)