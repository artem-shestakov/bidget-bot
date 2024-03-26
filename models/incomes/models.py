from ..base import Base
from sqlalchemy import ForeignKey, BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class Income(Base):
    title: Mapped[str]
    plan_amount: Mapped[int] = mapped_column(nullable=True)
    budget_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("budget.id"))
