from datetime import datetime
from pathlib import Path
from typing import List

import pandas as pd
import pytz
import torch
from config.core import params
from pymongo.cursor import Cursor
from schemas import RecommendationResponse


def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def try_gpu(i=0) -> torch.device:
    if torch.cuda.device_count() >= i + 1:
        return torch.device(f"cuda:{i}")
    return torch.device("cpu")


def parse_to_response(histories_cursor: Cursor) -> List[RecommendationResponse]:
    return [RecommendationResponse.parse_obj(cursor) for cursor in histories_cursor]


def get_now_date() -> str:
    tz = pytz.timezone(params["timezone"])
    return datetime.now(tz).isoformat()
