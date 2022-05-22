from sqlalchemy import select

from app.db.repositories.base import BaseRepository
from app.db.tables import SpecializationCategory, Specialization


class SpecializationCategoryRepository(BaseRepository):
    async def list_all(self):
        query = select(SpecializationCategory)
        return (await self.session.execute(query)).scalars().all()

    async def get_by_id(self, _id: str):
        query = select(SpecializationCategory).filter(SpecializationCategory.id == _id)
        return (await self.session.execute(query)).scalars().first()


class SpecializationRepository(BaseRepository):
    async def list_all(self):
        query = select(Specialization)
        return (await self.session.execute(query)).scalars().all()

    async def get_by_id(self, _id: str):
        query = select(Specialization).filter(Specialization.id == _id)
        return (await self.session.execute(query)).scalars().first()

    async def list_by_category_id(self, category_id: str):
        query = select(Specialization).filter(Specialization.specialization_category_id == category_id)
        return (await self.session.execute(query)).scalars().all()
