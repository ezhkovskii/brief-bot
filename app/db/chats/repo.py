"""Chat repo."""

from typing import List

from app.db.crud import CRUD
from app.db.sqlalchemy import AsyncSession
from app.db.chats.models import ChatModel
from app.schemas.chats import ChatDB
from app.logger import logger



class ChatRepo:
    def __init__(self, session: AsyncSession):
        """Initialize repo with CRUD."""
        self._crud = CRUD(session=session, cls_model=ChatModel)


    async def get_or_none(self, record_id: str) -> ChatDB | None:
        record = await self._crud.get_or_none(pkey_val=record_id)
        return ChatDB.model_validate(record) if record else None

    
    async def create(self, data: dict) -> ChatDB:
        """Create record row in db."""
        row = await self._crud.create(model_data=data)
        record_from_db = await self._crud.get(pkey_val=row.id)
        chat = ChatDB.model_validate(record_from_db)
        logger.info(f"Чат создан {chat}")
        return chat


    async def update(self, record_id: str, model_data: dict) -> ChatDB:
        """Update record row in db."""
        await self._crud.update(
            pkey_val=record_id,
            model_data=model_data,
        )
        record_from_db = await self._crud.get(pkey_val=record_id)
        chat = ChatDB.model_validate(record_from_db)
        logger.info(f"Чат обновлен {chat}")
        return chat