from .base import Base
from sqlalchemy.orm import Mapped

class Income(Base):
    title: Mapped[str]
    plan_amount: Mapped[int]
