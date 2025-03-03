import pytest_asyncio
from datetime import date
from sqlmodel import select
from database.scrapping import insert_doe
from models.models import DOECreate


@pytest_asyncio.fixture()
async def test_insert_doe(session):
    filename = "do20250103p02.pdf"
    doe = DOECreate(filename)
    insert_doe(session, doe)

    result = await session.execute(select(DOE))

    assert result is not None
    assert result.filename == "do20250103p02.pdf"
    assert result.data_publicacao == date(2025, 1, 3)
    assert result.caderno == 2

