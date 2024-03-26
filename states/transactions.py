from aiogram.fsm.state import State, StatesGroup

class TopUpState(StatesGroup):
    select_income = State()
    create_topup = State()
