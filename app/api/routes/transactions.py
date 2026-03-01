from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.transaction_schema import TransferRequest, TransactionResponse
from app.services.transaction_service import transfer_funds
from app.core.dependencies import get_db

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.post("/transfer", response_model=TransactionResponse)
def transfer(request: TransferRequest, db: Session = Depends(get_db)):
    try:
        tx = transfer_funds(db, request.from_account, request.to_account, request.amount)
        return tx
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))