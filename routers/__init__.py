from aiogram import Router
from .incomes import router as incomes_router

router = Router()
router.include_router(incomes_router)