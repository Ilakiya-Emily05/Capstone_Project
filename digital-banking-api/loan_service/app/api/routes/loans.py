from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.loan_schema import LoanCreate, LoanResponse
from app.services.loan_service import create_loan, approve_loan, reject_loan, get_loan, get_pending_loans

router = APIRouter(prefix="/loans", tags=["loans"])

@router.post("/apply", response_model=LoanResponse)
def apply_loan(loan: LoanCreate, db: Session = Depends(get_db)):
    return create_loan(db, loan.user_id, loan.amount, loan.interest_rate)

@router.get("/pending", response_model=list[LoanResponse])
def list_pending_loans(db: Session = Depends(get_db)):
    return get_pending_loans(db)

@router.put("/{loan_id}/approve", response_model=LoanResponse)
def approve_loan_endpoint(loan_id: str, db: Session = Depends(get_db)):
    loan = approve_loan(db, loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan

@router.put("/{loan_id}/reject", response_model=LoanResponse)
def reject_loan_endpoint(loan_id: str, db: Session = Depends(get_db)):
    loan = reject_loan(db, loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan