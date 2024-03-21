from sqlalchemy.ext.asyncio import AsyncSession
from .models import Budget


async def create_budget(session: AsyncSession, chat_id: int) -> Budget:
    # session = database.get_scoped_session()
    budget = Budget(
        chat_id=chat_id
    )
    session.add(budget)
    await session.commit()
    return budget
