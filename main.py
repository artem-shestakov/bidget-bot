import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.bot import DefaultBotProperties
from core.config import BOT_TOKEN
from core.database import database
from models import Base
from routers import router
from routers.start import start_cmd, join_to_group
from states.incomes import CreateIncomeState
from utils.commands import set_commands
from middleware import DBSessionMiddleware


async def db_init():
    async with database.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

default = DefaultBotProperties(parse_mode='html')

bot = Bot(BOT_TOKEN, default=default)
dp = Dispatcher()
dp.include_router(router)
dp.startup.register(db_init)

async def run():
    dp.update.middleware(DBSessionMiddleware(database.sessions_factory))
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(run())