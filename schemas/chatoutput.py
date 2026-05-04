from pydantic import BaseModel,HttpUrl
from typing import List,Optional



class Source(BaseModel):
    url:List[HttpUrl]
    content:str

class modeloutput(BaseModel):
    response:str
    sources:List[Source]
    followup_questions:List[str]

    