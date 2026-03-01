from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.account_schema import AccountCreate, AccountResponse
from app.services.account_service import create_new_account, get_account
from app.core.dependencies import get_db

router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.post("/", response_model=AccountResponse)
def create_account_route(account: AccountCreate, db: Session = Depends(get_db)):
    try:
        acc = create_new_account(db, user_id=account.user_id, initial_deposit=account.balance)
        return acc
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{account_id}", response_model=AccountResponse)
def get_account_route(account_id: int, db: Session = Depends(get_db)):
    acc = get_account(db, account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc