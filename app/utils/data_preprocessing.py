import pandas as pd
import numpy as np
from config.core import params, APP_ROOT
from utils.helper import load_data


def fillna_with_whitspace(df, features) -> None:
    _ = [df[column].fillna("", inplace=True) for column in features]


def create_user_prompt(df: pd.DataFrame) -> pd.Series:
    return (
        "Area de "
        + df.area
        + " - "
        + df.subareas
        + ", en "
        + df.country
        + " o remoto. Con modalidad "
        + df.work_modality
        + ". "
        + df.hardskills
    )


def create_job_prompt(df: pd.DataFrame) -> pd.Series:
    place: np.ndarray = np.where(df.remote, "Remoto", df.country)

    return (
        "Area de "
        + df.area
        + ", "
        + place
        + ", con modalidad "
        + df.work_modality
        + ". "
        + df.description
    )


def process_data(path: str) -> None:
    data = load_data(APP_ROOT.parent / params["data"]["raw"][path]).copy()
    fillna_with_whitspace(data, params["features_na"][path])
    processed_path = APP_ROOT.parent / params["data"]["processed"][path]

    if path == "users":
        data["prompt"] = create_user_prompt(data)
        data[["id_user", "prompt"]].to_csv(processed_path)
    else:
        print("creating job dataset...")
        data["prompt"] = create_job_prompt(data)
        data[["prompt"]].to_csv(processed_path)
