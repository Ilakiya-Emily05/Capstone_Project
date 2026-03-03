from sqlalchemy.orm import Session
from app.models.account import Account

def create_account(db: Session, user_id: int, initial_balance: float = 0.0):
    account = Account(user_id=user_id, balance=initial_balance)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def get_account(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def freeze_account(db: Session, account_id: int):
    account = get_account(db, account_id)
    if account:
        account.status = "FROZEN"
        db.commit()
        db.refresh(account)
    return account

def unfreeze_account(db: Session, account_id: int):
    account = get_account(db, account_id)
    if account:
        account.status = "ACTIVE"
        db.commit()
        db.refresh(account)
    return account