from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Dict, Callable, Awaitable
from sqlalchemy.ext.asyncio import async_sessionmaker, async_scoped_session


class DBSessionMiddleware(BaseMiddleware):
    def __init__(self, session) -> None:
        self.session = session

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        async with self.session() as session:
            data['session'] = session
            return await handler(event, data)