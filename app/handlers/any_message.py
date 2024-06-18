from collections import defaultdict
from aiogram import F, Bot, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from dishka.integrations.aiogram import FromDishka, inject, setup_dishka

from g4f.client import Client



from app.logger import logger
from app.schemas.messages import MessageDB
from app.schemas.users import UserDB
from app.services.messages import MessageService
from app.services.users import UserService


router = Router()
messages = defaultdict(list)

@router.message(~F.text.startswith('/'))
async def any_message_handler(message: Message, message_service: FromDishka[MessageService], user_service: FromDishka[UserService]) -> None:
    # проверяем пользователя. есть ли в бд, если нет, то добавляем
    # проверяем что за сообщение, текст, аудио, видео и т д.
    # в зависимости от типа парсим в схему и добавляем в бд
    user_db = UserDB(
        id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        is_bot=message.from_user.is_bot,
        username=message.from_user.username
    )
    user = await user_service.get_or_create(user_db)

    message_db = MessageDB(
        id=message.message_id,
        date=message.date,
        text=message.text,
        chat_id=str(message.chat.id),
        user_id=user.id
    )
    if message.video_note:
        message_db.file_id = message.video_note.file_id
        #message_db.mime_type = message.video_note.mime_type
        message_db.file_size = message.video_note.file_size
    elif message.voice:
        message_db.file_id = message.voice.file_id
        message_db.mime_type = message.voice.mime_type
        message_db.file_size = message.voice.file_size

    
    message_db = await message_service.create(message_db)
    
