from typing import List

from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException

from app.api.dependencies.database import get_repository
from app.api.dependencies.filter.vacancy import BookFilterManager
from app.db.repositories.vacancy import VacancyAreaRepository, VacancyEmployerRepository, VacancyRepository
from app.schemas.filter.vacancy import VacancyFilter
from app.schemas.vacancy import VacancyAreaInResponse, VacancyEmployerInResponse, VacancyInResponse

router = APIRouter()

_employers = []
_areas = []


@router.get('/areas/', response_model=List[VacancyAreaInResponse],
            name='vacancy:vacancy-areas')
async def list_vacancy_areas(
        vacancy_area_repo: VacancyAreaRepository = Depends(get_repository(VacancyAreaRepository))
) -> List[VacancyAreaInResponse]:
    if len(_areas) == 0:
        for area in await vacancy_area_repo.list_all():
            _areas.append(
                VacancyAreaInResponse(
                    id=area.id,
                    label=area.name
                )
            )
    return _areas


@router.get('/areas/{area_id}/', response_model=VacancyAreaInResponse,
            name='specialization:specialization-category')
async def retrieve_vacancy_area(
        area_id: str,
        vacancy_area_repo: VacancyAreaRepository = Depends(get_repository(VacancyAreaRepository))
) -> VacancyAreaInResponse:
    area = await vacancy_area_repo.get_by_id(area_id)
    if area is None:
        raise HTTPException(status_code=404, detail='Area not found')

    return area


@router.get('/employers/', response_model=List[VacancyEmployerInResponse],
            name='vacancy:vacancy-employers')
async def list_vacancy_employers(
        vacancy_employer_repo: VacancyEmployerRepository = Depends(get_repository(VacancyEmployerRepository))
) -> List[VacancyEmployerInResponse]:
    global _employers
    if len(_employers) == 0:
        employers = await vacancy_employer_repo.list_all()
        for employer in employers:
            _employers.append(
                VacancyEmployerInResponse(
                    id=employer.id,
                    name=employer.name
                )
            )
    return _employers


@router.get('/employers/{employer_id}/', response_model=VacancyEmployerInResponse,
            name='vacancy:vacancy-employer')
async def retrieve_vacancy_employer(
        employer_id: str,
        vacancy_employer_repo: VacancyEmployerRepository = Depends(get_repository(VacancyEmployerRepository))
) -> VacancyEmployerInResponse:
    employer = await vacancy_employer_repo.get_by_id(employer_id)
    if employer is None:
        raise HTTPException(status_code=404, detail='Employer not found')

    return employer


vacancy_filter_manager = BookFilterManager(
    ['official', 'living', 'vacation', 'coworkers', 'office', 'education', 'salary_bonus', 'location', 'extra',
     'growth',
     'tasks', 'dms', 'social', 'discount', 'hours', 'disko', 'food', 'remote', 'drive', 'hotel', 'tech', 'clothes',
     'sport']
)


@router.get('/', response_model=List[VacancyInResponse],
            name='vacancy:vacancies')
async def list_filtered_vacancies(
        vacancy_filter: VacancyFilter = Depends(vacancy_filter_manager),
        vacancy_repo: VacancyRepository = Depends(get_repository(VacancyRepository))
) -> List[VacancyInResponse]:
    vacancies = await vacancy_repo.list_filtered(
        area_id=vacancy_filter.area_id,
        specialization_id=vacancy_filter.specialization_id,
        employer_id=vacancy_filter.employer_id,
        bonuses=vacancy_filter.bonuses
    )

    return vacancies


@router.get('/{vacancy_id}/', response_model=VacancyInResponse, name='vacancy:vacancy')
async def retrieve_vacancy(
        vacancy_id: str,
        vacancy_repo: VacancyRepository = Depends(get_repository(VacancyRepository))
) -> VacancyInResponse:
    vacancy = await vacancy_repo.get_by_id(vacancy_id)
    return vacancy
