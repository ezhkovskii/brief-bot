"""Chat repo."""

from typing import List

from app.db.crud import CRUD
from app.db.sqlalchemy import AsyncSession
from app.db.users.models import UserModel
from app.schemas.users import UserDB
from app.logger import logger



class UserRepo:
    def __init__(self, session: AsyncSession):
        """Initialize repo with CRUD."""
        self._crud = CRUD(session=session, cls_model=UserModel)


    async def get_or_none(self, record_id: int) -> UserDB | None:
        record = await self._crud.get_or_none(pkey_val=record_id)
        return UserDB.model_validate(record) if record else None

    
    async def create(self, data: dict) -> UserDB:
        """Create record row in db."""
        row = await self._crud.create(model_data=data)
        record_from_db = await self._crud.get(pkey_val=row.id)
        chat = UserDB.model_validate(record_from_db)
        logger.info(f"Пользователь создан {chat}")
        return chat


    async def update(self, record_id: int, model_data: dict) -> UserDB:
        """Update record row in db."""
        await self._crud.update(
            pkey_val=record_id,
            model_data=model_data,
        )
        record_from_db = await self._crud.get(pkey_val=record_id)
        chat = UserDB.model_validate(record_from_db)
        logger.info(f"Пользователь обновлен {chat}")
        return chat