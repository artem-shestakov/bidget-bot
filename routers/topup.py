from aiogram import Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from models.incomes import crud as incomes_crud, IncomeCallback
from models.transactions import crud as transaction_crud, Topup
from sqlalchemy.ext.asyncio import AsyncSession
from states.transactions import TopUpState
import datetime
import re
import time


router = Router(name=__name__)


@router.message(F.text.regexp(r"^\+(\d+)(.*)?"))
async def start_top_up(message: Message, bot: Bot, state: FSMContext, session: AsyncSession):
    m = re.search(r"^\+(\d+)(.*)?", message.text)
    print(m.group(1), m.group(2))
    
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
    await state.update_data(amount=m.group(1))
    await state.update_data(description=m.group(2).strip())
    await state.set_state(TopUpState.select_income)

@router.callback_query(TopUpState.select_income)
async def create_topup(callback_query: CallbackQuery, bot: Bot, state: FSMContext, session: AsyncSession):
    await callback_query.answer()
    data = await state.get_data()
    topup = Topup(income_id=int(callback_query.data.split(":")[1]), amount=float(data["amount"]),description=data["description"], date=datetime.datetime.now().strftime('%s'))
    await transaction_crud.create_topup(session, topup)
    await state.clear()
