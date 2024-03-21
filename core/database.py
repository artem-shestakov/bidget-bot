from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from core.config import DB_URL


class Database:
    def __init__(self, db_url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=db_url,
            echo=echo
        )
        self.sessions = async_sessionmaker(
            bind=self.engine,
            autocommit=False
        )

database = Database(db_url=DB_URL, echo=True)