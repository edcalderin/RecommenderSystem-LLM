from fastapi import APIRouter, Request
from controllers import recommendation_controller
from schemas import RecommendationResponse

recommender_router = APIRouter()


@recommender_router.get(
    "/{id_user}",
    summary="Get recommendations endpoint",
    description="Get a list of job recommendations by an existing user id",
    response_model=RecommendationResponse,
)
def get_recommendations_by_id(id_user: int, request: Request):
    return recommendation_controller.get_recommendatios_by_id(id_user, request)
