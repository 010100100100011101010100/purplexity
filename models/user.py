#userid, agents:[], chats:[], createdat, email

from core.db import user_collection
from datetime import datetime
import random
from letta import Letta

def createUser(email:str):
    user_doc={
        "userId":random.randint(1,500000),
        "email":email,
        "createdat":datetime.now(),
        "agents":[]
    }
    result=user_collection.insert_one(user_doc)
    return str(result.inserted_id)

def get_user_details(userId):
    result=user_collection.find_one({"userId":userId})
    return result


