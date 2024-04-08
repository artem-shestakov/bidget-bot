from aiogram import Router
from .start import router as start_router
from .incomes import router as incomes_router
from .expenses import router as expense_router
from .topup import router as topup_router

router = Router()
router.include_router(start_router)
router.include_router(incomes_router)
router.include_router(expense_router)
router.include_router(topup_router)
