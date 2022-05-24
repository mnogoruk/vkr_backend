from datetime import datetime
from typing import List, Optional

from app.schemas.rwschema import RWSchema
from app.schemas.specialization import SpecializationInResponse


class VacancyAreaInResponse(RWSchema):
    id: str
    label: Optional[str]
    name: Optional[str]


class VacancyEmployerInResponse(RWSchema):
    id: str
    name: str


class VacancyInResponse(RWSchema):
    id: str
    name: str
    alternate_url: str
    description_cleaned: str

    area: VacancyAreaInResponse
    employer: VacancyEmployerInResponse
    specializations: List[SpecializationInResponse]

    published_at: datetime
    created_at: datetime

    official: bool
    living: bool
    vacation: bool
    coworkers: bool
    office: bool
    education: bool
    salary_bonus: bool
    location: bool
    extra: bool
    growth: bool
    tasks: bool
    dms: bool
    social: bool
    discount: bool
    hours: bool
    disko: bool
    food: bool
    remote: bool
    drive: bool
    hotel: bool
    tech: bool
    clothes: bool
    sport: bool
