import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command, JOIN_TRANSITION
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter
# from dotenv import load_dotenv
from handlers.init import start_init
from handlers.start import start_cmd, join_to_group
from utils.commands import set_commands


# load_dotenv()
token = os.getenv('BOT_TOKEN')
default = DefaultBotProperties(parse_mode='html')

bot = Bot(token, default=default)
dp = Dispatcher()

# Start
dp.message.register(start_cmd, Command(commands="start"))
dp.my_chat_member.register(join_to_group, ChatMemberUpdatedFilter(JOIN_TRANSITION))

# Init budget
dp.message.register(start_init, F.text=="🚀 Начать")

async def run():
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(run())