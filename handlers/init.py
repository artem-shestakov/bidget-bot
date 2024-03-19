from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.init import InitState

async def start_init(message: Message, state: FSMContext):
    await message.answer("""
Отлично!!
Для начала создадим первый источник дохода 💶.
Для этого ввидите его <b>название</b> и/или <b>плановый доход</b> через пробел.
Плановый доход вводить не обязательно.

Например так:
💳 Зарплата 100000

или так
💰 Фриланс
    """)

    await state.set_state(InitState.initIncomes)
