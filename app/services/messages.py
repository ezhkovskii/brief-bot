from sqlalchemy.ext.asyncio import AsyncSession

from app.db.messages.repo import MessageRepo
from app.schemas.messages import MessageDB
from app.logger import logger


class MessageService:

    def __init__(self, repo: MessageRepo) -> None:
        self._repo = repo
    
    async def create(self, message_db: MessageDB) -> MessageDB:
        message = await self._repo.create(message_db.model_dump())
        return message
