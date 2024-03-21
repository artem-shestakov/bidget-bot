from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from keyboards.incomes import incomes_kb
from states.incomes import CreateIncomeState


router = Router(name=__name__)

@router.message(Command("incomes"))
async def get_incomes(message: Message, bot: Bot, counter):
    await bot.send_message(
        message.chat.id,
        "Ваши источники дохода:",reply_markup=incomes_kb
    )
    print(counter)
    pass

@router.callback_query(F.data == "__add_income")
async def add_income(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.answer("""
Я помогу создать источник дохода 💶.
Для этого ввидите его <b>название</b> и/или <b>плановый доход</b> через пробел.
<b>Название</b> может стоять из нескольких слов.
<b>Плановый доход</b> вводить не обязательно.

Вот пару примеров:
💳 Зарплата 100000
💰 Фриланс
🥦 Продажа овощей 50000
""")

    await state.set_state(CreateIncomeState.create_income)

@router.message(CreateIncomeState.create_income)
async def create_income(message: Message, state: FSMContext):
    print(message.text)
    pass