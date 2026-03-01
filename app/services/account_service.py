from app.repositories.account_repository import create_account, get_account_by_id, update_balance
import random

def generate_account_number():
    return str(random.randint(10**9, 10**10 - 1))  # 10-digit unique number

def create_new_account(db, user_id: int, initial_deposit: float):
    account_number = generate_account_number()
    return create_account(db, user_id=user_id, account_number=account_number, initial_balance=initial_deposit)

def get_account(db, account_id: int):
    return get_account_by_id(db, account_id)