from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

init_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 Начать!",
                callback_data="__startup"),
            InlineKeyboardButton(
                text="Пропустить",
                callback_data="__skip_startup")
        ],
    ])