from dishka import make_async_container

from app.ioc.chats import ChatProvider
from app.ioc.database import DatabaseProvider
from app.ioc.g4f import G4FProvider
from app.ioc.messages import MessageProvider
from app.ioc.users import UserProvider


container = make_async_container(
    DatabaseProvider(), 
    G4FProvider(),
    ChatProvider(),
    UserProvider(),
    MessageProvider(),
) 