from fastapi import APIRouter

from .history_routers import history_router
from .recommender_routers import recommender_router
from .root_routers import root_router

router = APIRouter()

router.include_router(
    recommender_router, tags=["Recommendations"], prefix="/recommendations"
)
router.include_router(history_router, tags=["History"], prefix="/history")
