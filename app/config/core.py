import os

from typing import Dict

import yaml
from loguru import logger
from pydantic import BaseSettings

from app import APP_ROOT

CONFIG_FILE_PATH = APP_ROOT / "params.yaml"


def load_params() -> Dict:
    try:
        with open(CONFIG_FILE_PATH, "r") as file:
            params = yaml.safe_load(file)
        return params
    except (Exception, FileNotFoundError) as e:
        logger.error("An exception ocurred:", e)


class Envs(BaseSettings):
    MONGO_DB: str = os.environ["MONGO_DB"]
    MONGO_PORT: int = int(os.environ["MONGO_PORT"])
    MONGO_HOST: str = os.environ["MONGO_HOST"]

    HOST: str = os.environ["HOST"]
    PORT: int = int(os.environ["PORT"])


params = load_params()
envs = Envs()
