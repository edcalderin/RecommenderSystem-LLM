from datetime import datetime
from pathlib import Path
from typing import List

import pandas as pd
import pytz
from config.core import params
from pymongo.cursor import Cursor
from schemas import RecommendationResponse


def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def parse_to_response(histories_cursor: Cursor) -> List[RecommendationResponse]:
    return [RecommendationResponse.parse_obj(cursor) for cursor in histories_cursor]


def get_now_date() -> str:
    tz = pytz.timezone(params["timezone"])
    return datetime.now(tz).isoformat()
