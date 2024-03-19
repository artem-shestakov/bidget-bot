from aiogram.fsm.state import State, StatesGroup

class InitState(StatesGroup):
    initIncomes = State()
    initCategories = State()