from asyncio import current_task
from core.config import DB_URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession


class Database:
    def __init__(self, db_url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=db_url,
            echo=echo
        )
        self.sessions_factory = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            expire_on_commit=False
        )
    
    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.sessions_factory,
            scopefunc= current_task
        )
        
        return session

database = Database(db_url=DB_URL, echo=True)