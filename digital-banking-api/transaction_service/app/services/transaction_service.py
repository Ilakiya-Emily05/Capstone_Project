from sqlalchemy.orm import Session
from app.models.transaction import Transaction

def create_transaction(db: Session, from_account: str, to_account: str, amount: float, type: str):
    txn = Transaction(from_account=from_account, to_account=to_account, amount=amount, type=type)
    db.add(txn)
    db.commit()
    db.refresh(txn)
    return txn

def get_transaction(db: Session, txn_id: str):
    return db.query(Transaction).filter(Transaction.id == txn_id).first()