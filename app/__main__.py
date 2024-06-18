import asyncio
from collections import defaultdict
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from dishka import Provider, Scope, make_async_container, provide
from dishka.integrations.aiogram import FromDishka, inject, setup_dishka

from sqlalchemy.ext.asyncio import AsyncSession


from g4f.client import Client

from app.db.sqlalchemy import build_db_session_factory, close_db_connections, get_db
from app.ioc.container import container
from app.ioc.g4f import G4FProvider
from app.settings import settings
from app.handlers.routers import router
from app.middlewares import register_middlewares
  

async def main() -> None:
    bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    register_middlewares(dp)
   
    setup_dishka(container=container, router=dp, auto_inject=True)

    try:
        await dp.start_polling(bot)
    finally:
        await container.close()
        await bot.session.close()



if __name__ == "__main__":
    asyncio.run(main())
