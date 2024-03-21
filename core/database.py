from sqlalchemy.exc.asyncio import create_async_engine

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost/postgres")
