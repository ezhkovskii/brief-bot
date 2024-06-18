from aiogram import Bot, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.logger import logger


router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer("Привет!")
