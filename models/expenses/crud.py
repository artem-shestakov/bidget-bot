from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from models.budget import Budget
from .models import Income


async def get_incomes(session: AsyncSession, chat_id: int) -> list[Income]:
    budget_stm = select(Budget).where(Budget.chat_id == chat_id)
    result: Result = await session.execute(budget_stm)
    budget = result.scalar()

    products_stm = select(Income).where(Income.budget_id == budget.id).order_by(Income.id)
    result: Result = await session.execute(products_stm)
    products = result.scalars().all()
    return list(products)

async def create_income(session: AsyncSession, income: Income):
    session.add(income)
    try:
        await session.commit()
    except IntegrityError as exc:
        print(exc)
    except Exception as exc:
        print(exc)
    return income