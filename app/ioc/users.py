from dishka import Provider, Scope, provide


from sqlalchemy.ext.asyncio import AsyncSession

from app.db.users.repo import UserRepo
from app.services.users import UserService



class UserProvider(Provider):
   
    @provide(scope=Scope.REQUEST)
    def repo(self, session: AsyncSession) -> UserRepo:
        return UserRepo(session=session)
    
    @provide(scope=Scope.REQUEST)
    def service(self, user_repo: UserRepo) -> UserService:
        return UserService(repo=user_repo)
