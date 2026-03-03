from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.routes import loans

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loan Service")
app.include_router(loans.router)