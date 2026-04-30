from pydantic import BaseClass,HttpUrl

class modeloutput:
    response:str
    sources:list[HttpUrl]
    followup_questions:list[str]

    