from app.repositories.account_repository import get_account_by_number, update_balance
from app.repositories.transaction_repository import create_transaction
import redis
from sqlalchemy.orm import Session

r = redis.Redis(host='localhost', port=6379, db=0)

def transfer_funds(db: Session, from_acc_num: str, to_acc_num: str, amount: float):
    lock_key = f"lock:{from_acc_num}"
    if not r.set(lock_key, "1", nx=True, ex=5):  # 5-second lock
        raise Exception("Transaction in progress. Try again.")

    try:
        from_account = get_account_by_number(db, from_acc_num)
        to_account = get_account_by_number(db, to_acc_num)
        if from_account.balance < amount:
            raise Exception("Insufficient funds")

        # Deduct and add
        update_balance(db, from_account, from_account.balance - amount)
        update_balance(db, to_account, to_account.balance + amount)

        # Record transaction
        tx = create_transaction(db, from_account=from_acc_num, to_account=to_acc_num, amount=amount, tx_type="transfer")
        return tx
    finally:
        r.delete(lock_key)