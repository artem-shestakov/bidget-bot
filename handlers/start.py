from aiogram import Bot
from aiogram.types import Message

async def start_cmd(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет')