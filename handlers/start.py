from aiogram import Bot
from aiogram.types import Message, ChatMemberUpdated

WELCOME_MSG = """
Привет! 👋
Я помогаю следить за финансами 🤑.

Нужна помощь? Запусти команду - /help
    """

async def start_cmd(message: Message, bot: Bot):
    await bot.send_message(
        message.chat.id,
        WELCOME_MSG)
    

async def join_to_group(chat: ChatMemberUpdated, bot: Bot):
    await chat.answer(WELCOME_MSG)
