import os
from datetime import date
from sqlmodel.ext.asyncio.session import AsyncSession

from database.models.models import DOE
from models.models import DOECreate


def insert_doe(session: AsyncSession, doe: DOECreate) -> None:
    ...
