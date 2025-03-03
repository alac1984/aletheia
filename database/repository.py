import os
from datetime import date
from sqlmodel.ext.asyncio.session import AsyncSession

from database.models.models import DOE
from models.models import DOECreate


async def insert_doe(session: AsyncSession, doe_create: DOECreate) -> None:
    doe = DOE(
        filename=doe_create.filename,
        data_publicacao = doe_create.data_publicacao,
        caderno=doe_create.caderno
    )
    session.add(doe)
    await session.commit()
