from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from app.config import test_get_db_url

test_database_url = test_get_db_url()
engine = create_async_engine(url=test_database_url)
test_async_session_maker = async_sessionmaker(engine, class_=AsyncSession)
