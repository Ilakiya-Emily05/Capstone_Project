from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from datetime import datetime

def create_transaction(
    db: Session,
    from_account: str,
    to_account: str,
    amount: float,
    tx_type: str
):
    transaction = Transaction(
        from_account=from_account,
        to_account=to_account,
        amount=amount,
        type=tx_type,
        created_at=datetime.utcnow()
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction