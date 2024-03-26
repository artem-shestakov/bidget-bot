from ..base import Base
from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class Transaction(Base):
    __abstract__ = True
    
    amount: Mapped[float] = mapped_column(nullable=False)
    description: Mapped[str]
    date: Mapped[str]

class Topup(Transaction):
    income_id: Mapped[int] = mapped_column(ForeignKey("incomes.id"))
