from fastapi import APIRouter
from typing import List

from controllers import history_controller
from schemas import RecommendationResponse

history_router = APIRouter()


@history_router.get(
    "/",
    summary="Get previous recommendations endpoint",
    description="Get previous recommendations ordered by date for all users or by specifying its id_user",
    response_model=List[RecommendationResponse],
)
async def get_history(id_user: int = None) -> List[RecommendationResponse]:
    return history_controller.get_history(id_user)
