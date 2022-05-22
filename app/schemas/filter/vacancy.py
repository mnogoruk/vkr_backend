from typing import Optional, List

from app.schemas.rwschema import RWSchema


class VacancyFilter(RWSchema):
    area_id: Optional[str] = None
    employer_id: Optional[str] = None
    specialization_id: Optional[str] = None
    bonuses: Optional[List[str]] = None
