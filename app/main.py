from config.core import envs, params
from config.intercept_handler import LOG_LEVEL, setup_logging
from config.startup import get_embedding_jobs, load_model
from fastapi import FastAPI
from loguru import logger
from routes import root_router, router
from utils.data_preprocessing import process_data
from uvicorn import Config, Server

app = FastAPI(title=params["app_name"])

app.include_router(root_router, tags=["Welcome"])
app.include_router(router, prefix="/api/v1")


@app.on_event("startup")
def starting():
    logger.info("Processing and saving users dataset")
    process_data("users")

    logger.info("Processing and saving jobs dataset")
    process_data("jobs")

    logger.info("Loading model")
    app.state.model = load_model()
    logger.info(f"Model running on {app.state.model.device}")

    logger.info("Generating embedding jobs")
    app.state.embedding_jobs = get_embedding_jobs(app.state.model)


if __name__ == "__main__":
    logger.info("Starting application...")

    server = Server(Config(app, host=envs.APP_HOST, port=envs.APP_PORT, log_level=LOG_LEVEL))

    setup_logging()

    server.run()
