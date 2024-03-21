from aiogram.fsm.state import State, StatesGroup

class CreateIncomeState(StatesGroup):
    income_name = State()
    create_income = State()
