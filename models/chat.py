#chatid, userid, agentid, createdat, {querie:[response,[sources]]},confidence_score,followups:[]

from pydantic import BaseModel
from core.db import chat_collection,user_collection,sources_collection
from datetime import datetime
from schemas import modelconfig
from bson import ObjectId
import random
from letta import Letta
import os
API_key=os.getenv("LETTA_API_KEY")
def create_chat(userId:str,model:str,query:str):
    client=Letta(api_key=API_key)
    agent_id=client.agents.create(
        model=model,
        memory_blocks=[
            {
                "label":"persona",
                "value":"You are an agent called Purplex determined to be the most optimised AI powered search engine for the user. You receive request plus scraped data on which you work, improve structure, add your own knowledge and share the result with the user"
            }
        ],
        description="This agent is designed to be the most optimised AI powered search engine for the user. It receives request plus scraped data on which it works, improves structure, adds its own knowledge and shares the result with the user",
        enable_sleeptime=True,
    ).id
    chat_doc={
        "chatId":random.randint(1,100000000),
        "userId":userId,
        "agentId":agent_id,
        "createdat":datetime.now(),
        "conversation_history":[{"role":"user","content":query}]
    }
    result=chat_collection.insert_one(chat_doc)
    return str(result.inserted_id)

def get_chat_details(chatId):
    result=chat_collection.find_one({'chatId':chatId})
    return result

def update_chat(chatId,query,response,sources,confidence_score,followups):
    chat_details=get_chat_details(chatId)
    conversation_history=chat_details['conversation_history']
    conversation_history.append({
        "query":query,
        "response":response,
        "sources":sources,
        "confidence_score":confidence_score,
        "followups":followups
    })
    chat_collection.update_one({'chatId':chatId},{"$set":{"conversation_history":conversation_history}})