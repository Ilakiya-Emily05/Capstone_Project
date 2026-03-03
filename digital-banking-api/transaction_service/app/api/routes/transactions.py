from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.transaction_schema import TransactionCreate, TransactionResponse
from app.services.transaction_service import create_transaction, get_transaction

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/", response_model=TransactionResponse)
def create_transaction_endpoint(txn: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, txn.from_account, txn.to_account, txn.amount, txn.type)

@router.get("/{txn_id}", response_model=TransactionResponse)
def get_transaction_endpoint(txn_id: str, db: Session = Depends(get_db)):
    txn = get_transaction(db, txn_id)
    if not txn:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return txn