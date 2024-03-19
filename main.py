import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command
from dotenv import load_dotenv
from handlers.start import start_cmd
from utils.commands import set_commands

load_dotenv()
token = os.getenv('BOT_TOKEN')
default = DefaultBotProperties(parse_mode='html')

bot = Bot(token, default=default)
dp = Dispatcher()

dp.message.register(start_cmd, Command(commands="start"))

async def run():
    await set_commands(bot)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(run())