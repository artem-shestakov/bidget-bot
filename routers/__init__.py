from aiogram import Router
from .incomes import router as incomes_router
from .start import router as start_router

router = Router()
router.include_router(incomes_router)
router.include_router(start_router)
