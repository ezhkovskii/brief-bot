from dishka import Provider, Scope, provide


from sqlalchemy.ext.asyncio import AsyncSession

from app.db.chats.repo import ChatRepo
from app.services.chats import ChatService



class ChatProvider(Provider):
   
    @provide(scope=Scope.REQUEST)
    def chat_repo(self, session: AsyncSession) -> ChatRepo:
        return ChatRepo(session=session)
    
    @provide(scope=Scope.REQUEST)
    def chat_service(self, chat_repo: ChatRepo) -> ChatService:
        return ChatService(repo=chat_repo)
