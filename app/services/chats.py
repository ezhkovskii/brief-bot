from sqlalchemy.ext.asyncio import AsyncSession

from app.db.chats.repo import ChatRepo
from app.schemas.chats import ChatDB
from app.logger import logger


class ChatService:

    def __init__(self, repo: ChatRepo) -> None:
        self._chat_repo = repo

    async def delete(self, chat_id: str) -> None:
        chat = await self._chat_repo.get_or_none(chat_id)
        if not chat:
            logger.warning(f"Чат не найден при удалении: {chat_id}")
            return
        
        await self._chat_repo.update(chat.id, {"deleted": True})
        return None
    
    async def create(self, chat_db: ChatDB) -> ChatDB:
        chat = await self._chat_repo.get_or_none(chat_db.id)
        if chat:
            chat = await self._chat_repo.update(chat.id, {"deleted": False})
        else:
            chat = await self._chat_repo.create(chat_db.model_dump())
        return chat
    