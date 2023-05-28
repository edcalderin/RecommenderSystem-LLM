from pymongo import MongoClient
from config.core import envs

uri = f"mongodb://{envs.MONGO_HOST}:{envs.MONGO_PORT}/admin"
client = MongoClient(uri)

db = client[envs.MONGO_DB]

history_collection = db["history_collection"]
