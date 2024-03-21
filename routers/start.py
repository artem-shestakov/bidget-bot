from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.types import Message, ChatMemberUpdated
from sqlalchemy.ext.asyncio import AsyncSession
from models.budget import crud
from aiogram.filters import Command, JOIN_TRANSITION
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter

router = Router(name=__name__)

WELCOME_MSG = """
Привет! 👋
Я помогаю следить за финансами 🤑.

Нужна помощь? Запусти команду - /help
    """

@router.message(Command("start"))
async def start_cmd(message: Message, bot: Bot, session: AsyncSession):
    await bot.send_message(
        message.chat.id,
        WELCOME_MSG)
    await crud.create_budget(session, message.chat.id)
    
@router.my_chat_member(ChatMemberUpdatedFilter(JOIN_TRANSITION))
async def join_to_group(chat: ChatMemberUpdated, bot: Bot, session: AsyncSession):
    await chat.answer(WELCOME_MSG)
    await crud.create_budget(session, chat.chat.id)
