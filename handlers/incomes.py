from aiogram import Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.incomes import incomes_kb
from states.incomes import CreateIncomeState

async def get_incomes(message: Message, bot: Bot):
    await bot.send_message(
        message.chat.id,
        "Ваши источники дохода:",reply_markup=incomes_kb
    )
    pass

async def add_income(message: Message, state: FSMContext):
    await message.answer("""
Я помогу создать источник дохода 💶.
Для этого ввидите его <b>название</b> и/или <b>плановый доход</b> через пробел.
<b>Название</b> может стоять из нескольких слов.
<b>Плановый доход</b> вводить не обязательно.

Вот пару примеров:
💳 Зарплата 100000
💰 Фриланс
🥦 Продажа овощей 50000
    """)

    await state.set_state(CreateIncomeState.createIncomes)

async def create_income(message: Message, state: FSMContext):
    print(message.text)
    pass