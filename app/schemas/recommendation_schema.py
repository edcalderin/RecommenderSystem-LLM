from typing import List, Optional

from pydantic import BaseModel


class Recommendation(BaseModel):
    match_score: float
    account_executive: Optional[float]
    area: str
    work_modality: str
    country: str
    city: str
    remote: bool
    vacancy_name: str
    description: str


class RecommendationResponse(BaseModel):
    id_user: int
    recommendation_date: str
    recommendations: List[Recommendation]
