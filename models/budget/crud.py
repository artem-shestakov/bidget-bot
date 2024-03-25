from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from .models import Budget


async def get_budget(session: AsyncSession, chat_id: int) -> Budget:
    budget_stm = select(Budget).where(Budget.chat_id == chat_id)
    result: Result = await session.execute(budget_stm)
    return result.scalar()

async def create_budget(session: AsyncSession, chat_id: int) -> Budget:
    budget = Budget(
        chat_id=chat_id
    )
    session.add(budget)
    try:
        await session.commit()
    except IntegrityError as exc:
        print(exc)
    except Exception as exc:
        print(exc)
    return budget

