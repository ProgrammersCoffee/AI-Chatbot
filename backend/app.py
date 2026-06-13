import os 
from typing import List,Dict 
from dotenv import load_dotenv
from fastapi import FastAPI ,HTTPException
from pydantic import BaseModel
from groq import Groq
from fastapi.middleware.cors import CORSMiddleware  # allows frontend to access backend 

load_dotenv()
GROQ_API_KEY=os.getenv("GROQ_API_KEY") 

# error handling for missing API key 
if not GROQ_API_KEY:
    raise ValueError("API key for groq is missing. please set the GROQ_API_KEY in.env file")


#turn on fastapi app 
app=FastAPI() 

#allow cors for frontend to access backend 
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


# use Groq client to connect to groq api 
client=Groq(api_key=GROQ_API_KEY)


# validation for incoming request body  # modified 
class UserInput(BaseModel):
    message:str
    role:str="user"
    conversation_id: str = "default_chat"  # modified #06.06.2026 


# Make a class for conversation recorder :  # like a book (instead of the database)
class conversation_recorder:
    def __init__(self):       # determine the personality of the bot .
        # type hinting 
        self.messages : list[dict[str,str]]=[{"role":"system","content":"You are a customer support representative."}] # system message to set the context for the conversation
        self.active:bool =True # to assure the conversation is working
        
# to hold active conversations in memory , # Global dictionary to store conversations by their ID.
conversations:dict[str,conversation_recorder]={} # temperory stock for conversations .



#the transporter    # function to query groq api and get response from the bot
def query_groq_api(conversation:conversation_recorder)->str:
    try:
       # sending the request to groq api,get response. 
       # creating the brain of the bot ,creating the respose.
        completion=client.chat.completions.create(
            model="Llama-3.1-8b-instant",#modified
            messages=conversation.messages ,# sending history to model.
            temperature=1.0,
            max_tokens=1024, #modified
            top_p=1.0,
            stream=True,# reponse will be chunk by chunk.. infront of user 
            stop=None,
          
        )
        # response of the bot .
        response=""
        for chunk in completion:
            response+=chunk.choices[0].delta.content or ""
        return response 
    
    except Exception as e:
        raise HTTPException(status_code=500,detail=F"Error with Groq api MOHAMED:{str(e)}")


    

    
# if the conversation there get it ,if not there create new one.
def get_or_create_conversation(conversation_id:str)->conversation_recorder:
    if conversation_id not in conversations:
        conversations[conversation_id]= conversation_recorder()
    return conversations[conversation_id] 
        
        
@app.post("/chat/")
async def chat(input: UserInput): # async make the function faster and receive more one request in the same time. 

    try:
        conversation=get_or_create_conversation(input.conversation_id) #modified
        # Append the user message to coversation history.
        conversation.messages.append({"role":input.role,"content":input.message})#modified
        

        # Append the bot response to conversation history (conversation_recorder)
        response=query_groq_api(conversation) #modified   # turn on the query_groq_api func to get response
        
    
        conversation.messages.append({"role":"assistant","content":response})  #modified
        # return the bot response to the frontend
        return{"response":response}
    except Exception as e:
        raise HTTPException(status_code=500,detail=F"Error processing the request: {str(e)}")


# using uvicorn 
if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000) 