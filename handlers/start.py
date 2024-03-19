from aiogram import Bot
from aiogram.types import Message, ChatMemberUpdated
from keyboards.init import init_kb

WELCOME_MSG = """
Привет! 👋
Я помогаю следить за финансами 🤑.

Если тебе нужна помощь запусти команду /help
    """

async def start_cmd(message: Message, bot: Bot):
    await bot.send_message(
        message.chat.id,
        WELCOME_MSG,
        reply_markup=init_kb)
    

async def join_to_group(chat: ChatMemberUpdated, bot: Bot):
    await chat.answer(WELCOME_MSG,
    reply_markup=init_kb)
