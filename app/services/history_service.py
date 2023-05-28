from typing import List

import dao.history_dao as history_dao
from schemas import RecommendationResponse


def get_history(id_user: int = None) -> List[RecommendationResponse]:
    return history_dao.find_history(id_user)


def save_recommendation(recommendation: RecommendationResponse) -> None:
    history_dao.insert_history(recommendation)
