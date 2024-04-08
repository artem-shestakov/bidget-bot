from aiogram.fsm.state import State, StatesGroup

class CreateExpenseCatState(StatesGroup):
    expense_cat_name = State()
    create_expense_cat = State()
