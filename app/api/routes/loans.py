# app/routes/loan_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.loan import Loan, LoanStatus
from app.schemas.loan_schema import LoanRequest, LoanResponse
from app.models.account import Account
from app.dependencies import get_current_user, role_required
from app.core.database import get_db

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("/apply", response_model=LoanResponse)
def apply_loan(data: LoanRequest, db: Session = Depends(get_db), user=Depends(get_current_user)):
    loan = Loan(user_id=user.id, amount=data.amount, interest_rate=data.interest_rate)
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan

@router.get("/pending", response_model=list[LoanResponse])
def list_pending_loans(db: Session = Depends(get_db), officer=Depends(role_required("OFFICER"))):
    return db.query(Loan).filter(Loan.status == LoanStatus.PENDING).all()

@router.put("/{loan_id}/approve", response_model=LoanResponse)
def approve_loan(loan_id: str, db: Session = Depends(get_db), officer=Depends(role_required("OFFICER"))):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not loan or loan.status != LoanStatus.PENDING:
        raise HTTPException(status_code=404, detail="Loan not found or not pending")
    account = db.query(Account).filter(Account.user_id == loan.user_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="User account not found")
    try:
        loan.status = LoanStatus.APPROVED
        loan.approved_by = officer.id
        account.balance += loan.amount
        db.commit()
        db.refresh(loan)
        return loan
    except:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error approving loan")

@router.put("/{loan_id}/reject", response_model=LoanResponse)
def reject_loan(loan_id: str, db: Session = Depends(get_db), officer=Depends(role_required("OFFICER"))):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if not loan or loan.status != LoanStatus.PENDING:
        raise HTTPException(status_code=404, detail="Loan not found or not pending")
    loan.status = LoanStatus.REJECTED
    loan.approved_by = officer.id
    db.commit()
    db.refresh(loan)
    return loan