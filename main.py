import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.db.tables import *


async def main():
    engine = create_async_engine(
        'postgresql+asyncpg://postgres:1@localhost:5432/postgres'
    )
    session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

    async with session_maker() as session:
        async with session.begin():
            query = select(Vacancy.id)
            specs = (await session.execute(query)).fetchall()
            print(specs[0])


asyncio.run(main())