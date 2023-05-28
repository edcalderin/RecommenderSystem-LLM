from fastapi import Request
from loguru import logger
from typing import Dict, List

from services import history_service, recommender_service
from schemas import RecommendationResponse, Recommendation
from utils.helper import get_now_date


def get_recommendatios_by_id(id_user: int, request: Request) -> List[Dict]:

    logger.info(f"Creating recommendation for id: {id_user}")

    recommendation_list: List[Recommendation] = recommender_service.get_recommendations(id_user, request)

    recommendation = RecommendationResponse(
        id_user=id_user,
        recommendation_date=get_now_date(),
        recommendations=recommendation_list,
    )

    logger.info("Saving recommendation")

    history_service.save_recommendation(recommendation)

    return recommendation
