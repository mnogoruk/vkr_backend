from typing import Optional, List

from sqlalchemy import select

from app.db.repositories.base import BaseRepository
from app.db.tables import VacancyArea, VacancyEmployer, Vacancy, Specialization


class VacancyAreaRepository(BaseRepository):

    async def list_all(self):
        query = select(VacancyArea)
        return (await self.session.execute(query)).scalars().all()

    async def get_by_id(self, _id: str):
        query = select(VacancyArea).filter(VacancyArea.id == _id)
        return (await self.session.execute(query)).scalars().first()


class VacancyEmployerRepository(BaseRepository):

    async def list_all(self):
        query = select(VacancyEmployer)
        return (await self.session.execute(query)).scalars().all()

    async def get_by_id(self, _id: str):
        query = select(VacancyEmployer).filter(VacancyEmployer.id == _id)
        return (await self.session.execute(query)).scalars().first()


class VacancyRepository(BaseRepository):

    async def list_filtered(
            self,
            area_id: Optional[str] = None,
            employer_id: Optional[str] = None,
            specialization_id: Optional[str] = None,
            bonuses: Optional[List[str]] = None
    ):
        query = select(Vacancy)

        if area_id is not None:
            query = query.filter(Vacancy.area_id == area_id)
        if employer_id is not None:
            query = query.filter(Vacancy.employer_id == employer_id)
        if specialization_id is not None:
            query = query.filter(Vacancy.specializations.any(Specialization.id == specialization_id))

            if bonuses is not None:
                if len(bonuses) != 0:
                    for bonus in bonuses:
                        filed = getattr(Vacancy, bonus)
                        query = query.filter(filed == True)

        return (await self.session.execute(query)).scalars().all()

    async def get_by_id(self, _id: str):
        query = select(Vacancy).filter(Vacancy.id == _id)
        return (await self.session.execute(query)).scalars().first()
