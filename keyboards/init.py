from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

init_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚀 Начать")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Нажми '🚀 Начать'")