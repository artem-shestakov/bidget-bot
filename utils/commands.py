from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="Запуск бота"
        ),
        BotCommand(
            command="incomes",
            description="Источники дохода"
        ),
        BotCommand(
            command="expenses",
            description="Категории расходов"
        ),
        BotCommand(
            command="help",
            description="Помощь в работе с ботом"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())