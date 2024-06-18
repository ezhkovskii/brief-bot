from dishka import Provider, Scope, provide


from sqlalchemy.ext.asyncio import AsyncSession

from app.db.messages.repo import MessageRepo
from app.services.messages import MessageService



class MessageProvider(Provider):
   
    @provide(scope=Scope.REQUEST)
    def repo(self, session: AsyncSession) -> MessageRepo:
        return MessageRepo(session=session)
    
    @provide(scope=Scope.REQUEST)
    def service(self, repo: MessageRepo) -> MessageService:
        return MessageService(repo=repo)
