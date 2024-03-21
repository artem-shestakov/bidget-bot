import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command, JOIN_TRANSITION
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter
from core.config import BOT_TOKEN
from routers import router
from routers.start import start_cmd, join_to_group
from states.incomes import CreateIncomeState
from utils.commands import set_commands


# load_dotenv()

default = DefaultBotProperties(parse_mode='html')

bot = Bot(BOT_TOKEN, default=default)
dp = Dispatcher()
dp.include_router(router)

# Start
dp.message.register(start_cmd, Command(commands="start"))
dp.my_chat_member.register(join_to_group, ChatMemberUpdatedFilter(JOIN_TRANSITION))

# Income
# dp.message.register(get_incomes, Command(commands="incomes")
# dp.message.register(add_income, CreateIncomeState.income_name)
# dp.message.register(create_income, CreateIncomeState.create_income)

async def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(run())