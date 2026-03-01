from sqlalchemy.orm import Session
from app.models.account import Account

def create_account(
    db: Session,
    user_id: int,
    account_number: str,
    initial_balance: float
):
    account = Account(
        user_id=user_id,
        account_number=account_number,
        balance=initial_balance,
        status="ACTIVE"
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def get_account_by_id(db: Session, account_id: int):
    return db.query(Account).filter(Account.id == account_id).first()

def get_account_by_number(db: Session, account_number: str):
    return db.query(Account).filter(Account.account_number == account_number).first()

def update_balance(db: Session, account: Account, new_balance: float):
    account.balance = new_balance
    db.commit()
    db.refresh(account)
    return account