from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from keyboards.incomes import incomes_kb
from states.incomes import CreateIncomeState
from models.budget import crud as budget_crud
from models.incomes import crud as incomes_crud, Income, IncomeCallback
from sqlalchemy.ext.asyncio import AsyncSession


router = Router(name=__name__)

@router.message(Command("incomes"))
async def get_incomes(message: Message, bot: Bot, session: AsyncSession):
    # Empty keyboard
    incomes_kb = InlineKeyboardMarkup(inline_keyboard=[])
    # Get all incomes
    incomes = await incomes_crud.get_incomes(session, message.chat.id)

    # Create keyboard buttons
    builder= InlineKeyboardBuilder()
    for income in incomes:
        builder.button(
            text=income.title,
            callback_data=IncomeCallback(id=income.id, title=income.title)
        )
    builder.button(
        text="Добавить",
        callback_data="__add_income"
    )
    builder.adjust(1)

    # Send incomes
    await bot.send_message(
        message.chat.id,
        "Ваши источники дохода:",reply_markup=builder.as_markup()
    )

@router.callback_query(F.data == "__add_income")
async def add_income(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.delete()
    await callback_query.message.answer("""
Я помогу создать источник дохода 💶.
Для этого ввидите его <b>название</b> и/или <b>плановый доход</b> через пробел.
<b>Название</b> может стоять из нескольких слов.
<b>Плановый доход</b> вводить не обязательно.

Вот пара примеров:
💳 Зарплата 100000
💰 Фриланс
🥦 Продажа овощей 50000
""")
    await state.set_state(CreateIncomeState.create_income)

@router.message(CreateIncomeState.create_income)
async def create_income(message: Message, state: FSMContext, session: AsyncSession):
    # Get title and plan amount
    split_msg = message.text.split(" ")
    if split_msg[-1].isdigit():
        income = Income(
            title=(" ").join(split_msg[:-1]),
            plan_amount = float(split_msg[-1])
        )
    else:
        income = Income(
            title=message.text,
            plan_amount = 0
        )
    # Get budget
    budget = await budget_crud.get_budget(session, message.chat.id)

    # Create income
    income.budget_id = budget.id
    await incomes_crud.create_income(session, income)
    await state.clear()