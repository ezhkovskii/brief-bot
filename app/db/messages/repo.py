"""Message repo."""

from typing import List

from app.db.crud import CRUD
from app.db.sqlalchemy import AsyncSession
from app.db.messages.models import MessageModel
from app.logger import logger
from app.schemas.messages import MessageDB



class MessageRepo:
    def __init__(self, session: AsyncSession):
        """Initialize repo with CRUD."""
        self._crud = CRUD(session=session, cls_model=MessageModel)


    async def get_or_none(self, record_id: int) -> MessageDB | None:
        record = await self._crud.get_or_none(pkey_val=record_id)
        return MessageDB.model_validate(record) if record else None

    
    async def create(self, data: dict) -> MessageDB:
        """Create record row in db."""
        row = await self._crud.create(model_data=data)
        record_from_db = await self._crud.get(pkey_val=row.id)
        record = MessageDB.model_validate(record_from_db)
        logger.info(f"Сообщение создано {record}")
        return record


    async def update(self, record_id: int, model_data: dict) -> MessageDB:
        """Update record row in db."""
        await self._crud.update(
            pkey_val=record_id,
            model_data=model_data,
        )
        record_from_db = await self._crud.get(pkey_val=record_id)
        record = MessageDB.model_validate(record_from_db)
        logger.info(f"Сообщение обновлено {record}")
        return record