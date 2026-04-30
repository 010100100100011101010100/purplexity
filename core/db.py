from pymongo import MongoClient


mongourl=os.getenv("MONGO_URL")

client=MongoClient(mongourl)
db=client["purplexity"]


chat_collection=db["chat"]
sources_collection=db["sources"]
user_collection=db["users"]


