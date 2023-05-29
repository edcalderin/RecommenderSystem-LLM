from typing import List

import pandas as pd
from config.core import APP_ROOT, params
from fastapi import Request
from schemas import Recommendation
from sentence_transformers import util
from utils.helper import load_data


def get_recommendations(id_user: int, request: Request, num=5) -> List[Recommendation]:
    """
    Function to return a list job recommendations according to a single user.
    Parameters

    arguments: Argument object

    Return
    Returns a list of dictionaries

    """
    processed_users = load_data(APP_ROOT.parent / params["data"]["processed"]["users"])
    jobs = load_data(APP_ROOT.parent / params["data"]["raw"]["jobs"])

    prompt: str = processed_users[processed_users.id_user == id_user]["prompt"].values[
        0
    ]

    embedding_user = request.app.state.model.encode(prompt, convert_to_tensor=True)

    similarity_scores = util.pytorch_cos_sim(
        embedding_user, request.app.state.embedding_jobs
    )

    values, indices = similarity_scores.squeeze().sort(descending=True)

    recommendations: pd.DataFrame = recommendation_dataframe(jobs, indices, values, num)

    return [
        Recommendation.parse_obj(item)
        for item in recommendations.to_dict(orient="records")
    ]


def recommendation_dataframe(
    jobs: pd.DataFrame, indices, values, num: int
) -> pd.DataFrame:
    recommendations: pd.DataFrame = jobs[jobs.index.isin(indices[:num].tolist())]
    recommendations.insert(0, "match_score", values[:num].tolist(), True)
    return recommendations
