from app.handlers.common import router as common_router
from app.handlers.any_message import router as any_message_router
from app.handlers.summarize import router as summarize_router
from app.handlers.bot_add_group import router as add_group_router


from aiogram import Router


router = Router()

router.include_router(common_router)
router.include_router(summarize_router)
router.include_router(add_group_router)
router.include_router(any_message_router)