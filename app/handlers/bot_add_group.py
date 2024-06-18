from aiogram import F, Bot, Router
from aiogram.filters.chat_member_updated import \
    ChatMemberUpdatedFilter, LEAVE_TRANSITION, JOIN_TRANSITION
from aiogram.types import ChatMemberUpdated

from dishka.integrations.aiogram import FromDishka

from app.logger import logger
from app.schemas.chats import ChatDB
from app.services.chats import ChatService

router = Router()
router.my_chat_member.filter(F.chat.type.in_({"group", "supergroup"}))

chats_variants = {
    "group": "группу",
    "supergroup": "супергруппу"
}


@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=JOIN_TRANSITION
    )
)
async def bot_added_as_member(event: ChatMemberUpdated, bot: Bot, chat_service: FromDishka[ChatService]):
    chat_db = ChatDB(
        id=str(event.chat.id),
        type=event.chat.type,
        title=event.chat.title,
        deleted=False
    )
    await chat_service.create(chat_db)

    chat_info = await bot.get_chat(event.chat.id)
    if chat_info.permissions.can_send_messages:
        await event.answer(
            text=f"Привет! Спасибо, что добавили меня в "
                 f'{chats_variants[event.chat.type]} "{event.chat.title}" '
        )
    else:
        logger.info(f"Бот добавлен в группу {event.chat.id}, но не может отправлять сообщения")



@router.my_chat_member(
    ChatMemberUpdatedFilter(
        member_status_changed=LEAVE_TRANSITION
    )
)
async def bot_deleted(event: ChatMemberUpdated, chat_service: FromDishka[ChatService]):
    await chat_service.delete(chat_id=str(event.chat.id))