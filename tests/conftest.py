import os
import pytest
import pytest_asyncio
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

@pytest_asyncio.fixture
async def session():
    test_engine = create_async_engine(
        DATABASE_URL.replace("dese", "tests"),
        echo=False,
        future=True
    )

    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async_session = sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with async_session() as test_session:
        yield test_session

    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
