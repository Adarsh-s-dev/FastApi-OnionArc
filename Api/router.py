from fastapi import APIRouter

from Api.Controllers.test_controller import router as test_router

router = APIRouter()

router.include_router(test_router)
