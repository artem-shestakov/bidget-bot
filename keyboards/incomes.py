from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

incomes_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Добавить",
                callback_data="__add_income")
        ],
    ])