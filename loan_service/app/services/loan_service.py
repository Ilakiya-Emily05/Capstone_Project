from sqlalchemy.orm import Session
from app.models.loan import Loan, LoanStatus

def create_loan(db: Session, user_id: str, amount: float, interest_rate: float):
    loan = Loan(user_id=user_id, amount=amount, interest_rate=interest_rate)
    db.add(loan)
    db.commit()
    db.refresh(loan)
    return loan

def approve_loan(db: Session, loan_id: str):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if loan:
        loan.status = LoanStatus.APPROVED
        db.commit()
        db.refresh(loan)
    return loan

def reject_loan(db: Session, loan_id: str):
    loan = db.query(Loan).filter(Loan.id == loan_id).first()
    if loan:
        loan.status = LoanStatus.REJECTED
        db.commit()
        db.refresh(loan)
    return loan

def get_loan(db: Session, loan_id: str):
    return db.query(Loan).filter(Loan.id == loan_id).first()

def get_pending_loans(db: Session):
    return db.query(Loan).filter(Loan.status == LoanStatus.PENDING).all()