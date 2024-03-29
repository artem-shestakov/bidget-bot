from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Topup

async def create_topup(session: AsyncSession, topup: Topup):
    session.add(topup)
    try:
        await session.commit()
    except IntegrityError as exc:
        print(exc)
    except Exception as exc:
        print(exc)
    return topup