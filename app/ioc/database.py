from dishka import Provider, Scope, provide


from app.db.sqlalchemy import AsyncGeneratorSession, build_db_session_factory



class DatabaseProvider(Provider):
   
    @provide(scope=Scope.APP)
    async def db(self) -> AsyncGeneratorSession:
        db = await build_db_session_factory()
        async with db() as session:
            yield session
