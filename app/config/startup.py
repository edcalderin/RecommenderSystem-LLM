from sentence_transformers import SentenceTransformer
from utils.helper import load_data, try_gpu

from .core import APP_ROOT, params


def load_model() -> SentenceTransformer:
    model_name = params["sentence_transformer"]["model_name"]

    model = SentenceTransformer(model_name, device=try_gpu())

    return model.to(try_gpu())


def get_embedding_jobs(model: SentenceTransformer):
    processed_jobs = load_data(APP_ROOT.parent / params["data"]["processed"]["jobs"])

    return model.encode(processed_jobs["prompt"], convert_to_tensor=True)
