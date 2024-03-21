from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession


class BaseRAGRepository:
    def __init__(self, async_session: SQLAlchemyAsyncSession):
        self.async_session = async_session
