from ..base import Base
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class Budget(Base):
    __tablename__ = "budget"
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True)
