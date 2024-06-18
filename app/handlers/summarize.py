from collections import defaultdict
from aiogram import Bot, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from dishka.integrations.aiogram import FromDishka, inject, setup_dishka

from g4f.client import Client


from app.logger import logger


router = Router()

messages = defaultdict(list)

@router.message(Command("anekdot"))
async def summary_handler(message: Message, client: FromDishka[Client]) -> None:
    user_id = message.from_user.id
    model = "gpt-3.5-turbo"
    try:
        logger.info(f"ПОЛЬЗОВАТЕЛЬ {message.from_user.username}, ТЕКСТ {message.text}")
        messages[user_id].append({"role": "user", "content": "Расскажи анекдот"})
        completion = client.chat.completions.create(
            model=model,
            messages=messages[user_id]
        )
        completion_choices_item = completion.choices[0].to_json()
        messages[user_id].append(completion_choices_item["message"])
        await message.answer(completion.choices[0].message.content)
        
        # Send a copy of the received message
        # await message.send_copy(chat_id=message.chat.id)
    except TypeError as exc:
        # But not all the types is supported to be copied so need to handle it
        logger.info(repr(exc))
        await message.answer("Nice try!")