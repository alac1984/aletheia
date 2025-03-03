import pytest
from datetime import date
from sqlmodel import select
from database.scrapping import insert_doe
from database.models.models import DOE
from models.models import DOECreate


@pytest.mark.asyncio
async def test_insert_doe(session):
    filename = "do20250103p02.pdf"
    doe = DOECreate(filename=filename)
    await insert_doe(session, doe)

    results = await session.exec(select(DOE))
    result = results.one()

    assert result is not None
    assert result.filename == "do20250103p02.pdf"
    assert result.data_publicacao == date(2025, 1, 3)
    assert result.caderno == 2

