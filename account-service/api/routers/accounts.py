from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.account_schema import AccountCreate, AccountResponse
from app.services.account_service import create_account, get_account, freeze_account, unfreeze_account

router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.post("/", response_model=AccountResponse)
def create_account_endpoint(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(db, user_id=account.user_id, initial_balance=account.initial_balance)

@router.get("/{account_id}", response_model=AccountResponse)
def get_account_endpoint(account_id: int, db: Session = Depends(get_db)):
    acc = get_account(db, account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc

@router.put("/{account_id}/freeze", response_model=AccountResponse)
def freeze_account_endpoint(account_id: int, db: Session = Depends(get_db)):
    acc = freeze_account(db, account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc

@router.put("/{account_id}/unfreeze", response_model=AccountResponse)
def unfreeze_account_endpoint(account_id: int, db: Session = Depends(get_db)):
    acc = unfreeze_account(db, account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc