from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from keyboards.incomes import incomes_kb
from states.expenses import CreateExpenseCatState
from models.budget import crud as budget_crud
from models.expenses import crud as expenses_crud, ExpenseCategory, ExpenseCategoryCallback
from sqlalchemy.ext.asyncio import AsyncSession


router = Router(name=__name__)

@router.message(Command("expenses"))
async def get_incomes(message: Message, bot: Bot, session: AsyncSession):
    # Empty keyboard
    incomes_kb = InlineKeyboardMarkup(inline_keyboard=[])
    # Get all incomes
    expense_cats = await expenses_crud.get_expense_category(session, message.chat.id)

    # Create keyboard buttons
    builder= InlineKeyboardBuilder()
    for expense_cat in expense_cats:
        builder.button(
            text=expense_cat.title,
            callback_data=ExpenseCategoryCallback(id=expense_cat.id)
        )
    builder.button(
        text="Добавить",
        callback_data="__add_expense_cat"
    )
    builder.adjust(1)

    # Send incomes
    await bot.send_message(
        message.chat.id,
        "Ваши категории расходов:",reply_markup=builder.as_markup()
    )

@router.callback_query(F.data == "__add_expense_cat")
async def add_income(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.delete()
    await callback_query.message.answer("""
Я помогу создать категорию расходов.
Для этого ввидите её <b>название</b> и/или <b>плановый доход</b> через пробел.
<b>Название</b> может стоять из нескольких слов.
<b>Плановый доход</b> вводить не обязательно.

Вот пара примеров:
🚎 Общественный транспорт 1500
🛒 Супермаркет 35000
☕️ Кафе
""")
    await state.set_state(CreateExpenseCatState.create_expense_cat)

@router.message(CreateExpenseCatState.create_expense_cat)
async def create_income(message: Message, state: FSMContext, session: AsyncSession):
    # Get title and plan amount
    split_msg = message.text.split(" ")
    if split_msg[-1].isdigit():
        expense_cat = ExpenseCategory(
            title=(" ").join(split_msg[:-1]),
            plan_amount = float(split_msg[-1])
        )
    else:
        expense_cat = ExpenseCategory(
            title=message.text,
            plan_amount = 0
        )
    # Get budget
    budget = await budget_crud.get_budget(session, message.chat.id)

    # Create income
    expense_cat.budget_id = budget.id
    await expenses_crud.create_expense_cat(session, expense_cat)
    await state.clear()