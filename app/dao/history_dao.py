import pymongo
from typing import List

from .database import history_collection
from schemas import RecommendationResponse
from utils.helper import parse_to_response


def insert_history(response: RecommendationResponse) -> None:
    history_collection.insert_one(response.dict())


def find_history(id_user: int = None) -> List[RecommendationResponse]:
    pattern = id_user if id_user == None else {"id_user": id_user}

    cursor = history_collection.find(pattern).sort(
        "recommendation_date", pymongo.DESCENDING
    )

    return parse_to_response(cursor)
