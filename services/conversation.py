from letta import Letta
import os
from models.chat import create_chat,get_chat_details,update_chat
from schemas.chatinput import ChatInput
from schemas.chatoutput import ChatOutput

API=os.getenv("LETTA_API_KEY")
client=Letta(api_key=API)

def conversation(uid:str,user_query:str,model,chatId:str=None):
    """
    This function allows the user to start/continue an optimal AI powered search with Letta
    Users can input the request ƒor which the scrape service first performs a search/ gets the data from vector 
    embedding which then gets sent to Letta and finally Letta outputs in the output structure we programmed  
    """
    if not chatId:
        create_chat(uid,model,user_query)
        chat_doc=get_chat_details(chatId)
        agent_id=chat_doc['agentId']
        response=client.agents.messages.create(
            agent_id=agent_id,
            model=model,
            messages=user_query,
            streaming=True,
            reasoning=True,
            streaming_tokens=True
        )
        for chunk in response:
            print(chunk.choices[0])
        conversation_output=ChatOutput(
            response=response,
            chatId=chatId
        )
        confidence_score=conversation_output.confidence_score
        follow_up_questions=conversation_output.follow_up_questions
        update_chat(chatId,user_query, conversation_output,confidence_score,followups=follow_up_questions)
    else:
        response=client.agents.messages.create(
            agent_id=chatId,
            model=model,
            messages=user_query,
            streaming=True,
            reasoning=True,
            streaming_tokens=True
        )
        for chunk in response:
            print(chunk.choices[0])
        conversation_output=ChatOutput(
            response=response,
            chatId=chatId
        )
        confidence_score=conversation_output.confidence_score
        follow_up_questions=conversation_output.follow_up_questions
        update_chat(chatId,user_query, conversation_output,confidence_score,followups=follow_up_questions)
        

    
    
    