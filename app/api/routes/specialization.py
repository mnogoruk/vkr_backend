from typing import List

from fastapi import APIRouter, Depends
from starlette.exceptions import HTTPException

from app.api.dependencies.database import get_repository
from app.db.repositories.specialization import SpecializationCategoryRepository, SpecializationRepository
from app.schemas.specialization import SpecializationCategoryInResponse, SpecializationInResponse

router = APIRouter()

_specializations = []

@router.get('/categories/', response_model=List[SpecializationCategoryInResponse],
            name='specialization:specialization-categories')
async def list_categories(
        spec_cat_repo: SpecializationCategoryRepository = Depends(get_repository(SpecializationCategoryRepository))
) -> List[SpecializationCategoryInResponse]:
    tags = await spec_cat_repo.list_all()
    return tags


@router.get('/categories/{category_id}/', response_model=SpecializationCategoryInResponse,
            name='specialization:specialization-category')
async def retrieve_category(
        category_id: str,
        spec_cat_repo: SpecializationCategoryRepository = Depends(get_repository(SpecializationCategoryRepository))
) -> SpecializationCategoryInResponse:
    cat = await spec_cat_repo.get_by_id(category_id)
    if cat is None:
        raise HTTPException(status_code=404, detail='Specialization category not found')

    return cat


@router.get('/', response_model=List[SpecializationInResponse],
            name='specialization:specializations')
async def list_specializations(
        spec_repo: SpecializationRepository = Depends(get_repository(SpecializationRepository))
) -> List[SpecializationInResponse]:
    if len(_specializations) == 0:
        for spec in await spec_repo.list_all():
            _specializations.append(
                SpecializationInResponse(
                    id=spec.id,
                    label=spec.name,
                    laboring=spec.laboring,
                    specialization_category=SpecializationCategoryInResponse(
                        id=spec.specialization_category.id,
                        name=spec.specialization_category.name,
                    )
                )
            )
    return _specializations


@router.get('/{specialization_id}/', response_model=SpecializationInResponse,
            name='specialization:specialization')
async def retrieve_specialization(
        specialization_id: str,
        spec_repo: SpecializationRepository = Depends(get_repository(SpecializationRepository))
) -> SpecializationInResponse:
    spec = await spec_repo.get_by_id(specialization_id)
    return spec


@router.get('/by_category/{category_id}', response_model=List[SpecializationInResponse],
            name='specialization:specializations-by_category')
async def list_specializations_by_category(
        category_id: str,
        spec_repo: SpecializationRepository = Depends(get_repository(SpecializationRepository))
) -> List[SpecializationInResponse]:
    specs = await spec_repo.list_by_category_id(category_id)
    return specs
