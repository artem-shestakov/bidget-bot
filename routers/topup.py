from aiogram import Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from models.incomes import crud as incomes_crud, IncomeCallback
from sqlalchemy.ext.asyncio import AsyncSession
from states.transactions import TopUpState
import re


router = Router(name=__name__)


@router.message(F.text.regexp(r"^\+(\d+)(.*)?"))
async def start_top_up(message: Message, bot: Bot, state: FSMContext, session: AsyncSession):
    m = re.search(r"^\+(\d+)(.*)?", message.text)

    # Empty keyboard
    incomes_kb = InlineKeyboardMarkup(inline_keyboard=[])
    # Get all incomes
    incomes = await incomes_crud.get_incomes(session, message.chat.id)

    # Create keyboard buttons and add to keyboard
    inline_kb = [[InlineKeyboardButton(text=income.title, callback_data=IncomeCallback(id=income.id, title=income.title).pack())] for income in incomes]
    incomes_kb.inline_keyboard = inline_kb

    # Send incomes
    await bot.send_message(
        message.chat.id,
        "Выберете источник дохода",reply_markup=incomes_kb
    )

    await state.set_state(TopUpState.select_income)

@router.callback_query(TopUpState.select_income)
async def create_topup(callback_query: CallbackQuery, bot: Bot, state: FSMContext, session: AsyncSession):
    await callback_query.answer()
    # create top up here
    await state.clear()
