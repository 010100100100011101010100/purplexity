from pydantic import BaseModel
from letta import Letta
from core.constants import *


modelname=anthropic_model_name or openai_model_name
model_temp=model_temperature
max_tokens=max_tokens
timeout=llm_timeout
reasoningsteps=reasoning_steps
api_key=os.getenv("LETTA_API_KEY")
tools=tools


class ModelConfig(BaseModel):
    def __init__(self,modelname:str,model_temp:float,max_tokens:int,timeout:int,reasoningsteps:int):
        self.modelname=modelname
        self.model_temp=model_temp
        self.max_tokens=max_tokens
        self.timeout=timeout
        self.reasoningsteps=reasoningsteps
        self.client=Letta(api_key=api_key)
        
    def createagent(self,uid:str,name:str,description:str,tools:list[str]):
        agent=self.client.create_agent(
            model=self.modelname
            name=name,
            description=description,
            tools=tools
            reasoning=True
            reasoning_steps=self.reasoningsteps
            temperature=self.model_temp
            streaming=True
            max_tokens=self.max_tokens
        )
        return agent.id


        
    
    