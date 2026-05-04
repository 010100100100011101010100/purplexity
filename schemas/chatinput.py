from pydantic import BaseModel,Field,HttpUrl
from typing import List,Optional

#Validation for the input to the model. I can add more fields to this as well, depends on the context engineering.
class Source(BaseModel):
    content:str
    urls:list[HttpUrl]

class Message(BaseModel):
    role:str
    content:str

class modelinput(BaseModel):
    '''this class helps us validate the input being sent to the model from the webcrawler'''
    sources:List[Source]
    userquery:str
    conversation_history:Optional[List[Message]]
    
    


    