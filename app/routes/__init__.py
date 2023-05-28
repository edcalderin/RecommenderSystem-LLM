from fastapi import APIRouter

from .root_routers import root_router
from .recommender_routers import recommender_router
from .history_routers import history_router

router = APIRouter()

router.include_router(
    recommender_router, tags=["Recommendations"], prefix="/recommendations"
)
router.include_router(history_router, tags=["History"], prefix="/history")