from fastapi import APIRouter
from app.api.routes.specialization import router as specialization_router
from app.api.routes.vacancy import router as vacancy_router

router = APIRouter()
router.include_router(specialization_router, tags=["specialization"], prefix="/specializations")
router.include_router(vacancy_router, tags=["vacancy"], prefix="/vacancies")
