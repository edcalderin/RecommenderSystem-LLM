from typing import List

from fastapi import HTTPException, status
from loguru import logger
from schemas import RecommendationResponse
from services import history_service


def get_history(id_user: int = None) -> List[RecommendationResponse]:
    logger.info(f"Getting recommendations history for id: {id_user}")

    histories = history_service.get_history(id_user)

    if len(histories) or (len(histories) == 0 and id_user is None):
        return histories
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id {id_user} not found",
    )
