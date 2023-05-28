from typing import List

from controllers import history_controller
from fastapi import APIRouter
from schemas import RecommendationResponse

history_router = APIRouter()


@history_router.get(
    "/",
    summary="Get previous recommendations endpoint",
    description='''
    To return all previous recommendations or by user id. You must keep in mind that this
    endopoint can return one or many recommendations sorted recently, this is useful when the jobs dataset
    is upgraded and need to inspect how the results evolved accordingly.''',
    response_model=List[RecommendationResponse],
)
async def get_history(id_user: int = None) -> List[RecommendationResponse]:
    return history_controller.get_history(id_user)
