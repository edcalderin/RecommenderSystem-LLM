from sentence_transformers import SentenceTransformer
from utils.helper import load_data

from .core import APP_ROOT, params


def load_model() -> SentenceTransformer:
    model_name = params["sentence_transformer"]["model_name"]

    return SentenceTransformer(model_name)


def get_embedding_jobs(model: SentenceTransformer):
    processed_jobs = load_data(APP_ROOT.parent / params["data"]["processed"]["jobs"])

    return model.encode(processed_jobs["prompt"], convert_to_tensor=True)
