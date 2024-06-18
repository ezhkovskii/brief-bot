from app.db.users.repo import UserRepo
from app.schemas.users import UserDB
from app.logger import logger


class UserService:

    def __init__(self, repo: UserRepo) -> None:
        self._repo = repo
    
    async def get_or_create(self, user_db: UserDB) -> UserDB:
        user = await self._repo.get_or_none(user_db.id)
        if not user:
            user = await self._repo.create(user_db.model_dump())
            
        return user
    