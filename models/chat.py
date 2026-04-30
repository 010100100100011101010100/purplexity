#chatid, userid, agentid, createdat, {querie:[response,[sources]]},confidence_score,followups:[]

from pydantic import BaseModel
from core.db import chat_collection,user_collection,sources_collection
from datetime import datetime
from schemas import modelconfig
from bson import ObjectId
import random
