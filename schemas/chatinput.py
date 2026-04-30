from pydantic import BaseClass,Field,HttpUrl


class modelinput:
    '''this class helps us validate the input being sent to the model from the webcrawler'''
    sources:list[HttpUrl]=Field(...,description="This contains all the scraped sources either sent from Tavily or embedding vector")
    userquery:str
    conversation_history:list=None
    
    


    