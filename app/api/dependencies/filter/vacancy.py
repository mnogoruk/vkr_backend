from typing import Optional, List

from starlette.exceptions import HTTPException

from app.schemas.filter.vacancy import VacancyFilter


class BookFilterManager:
    validation_error = HTTPException

    def __init__(self, allowed_bonuses: List[str]):
        self.allowed_bonuses = allowed_bonuses

    def __call__(
            self,
            area_id: Optional[str] = None,
            employer_id: Optional[str] = None,
            specialization_id: Optional[str] = None,
            bonuses: Optional[str] = None
    ) -> VacancyFilter:
        if bonuses is not None:
            bonuses_split = [bonus.strip() for bonus in bonuses.split(',')]
            bonuses = [bonus for bonus in bonuses_split if bonus in self.allowed_bonuses]
        else:
            bonuses = []
        return VacancyFilter(
            area_id=area_id,
            employer_id=employer_id,
            specialization_id=specialization_id,
            bonuses=bonuses
        )
