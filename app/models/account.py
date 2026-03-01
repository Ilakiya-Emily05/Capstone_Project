# account.py
import uuid
from sqlalchemy import Column, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .base import Base
from .user import User

class Account(Base):
    __tablename__ = "accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    balance = Column(Float, default=0.0)

    user = relationship("User", back_populates="accounts")

    transactions_from = relationship(
        "Transaction",
        foreign_keys="Transaction.from_account_id",
        back_populates="from_account",
        lazy="select"
    )
    transactions_to = relationship(
        "Transaction",
        foreign_keys="Transaction.to_account_id",
        back_populates="to_account",
        lazy="select"
    )