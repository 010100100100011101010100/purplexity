from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def root():
    return {"message": "yo"}

#send endpoint -> fetches data from redis/scrapes using tavily, gathers resources and sends to letta
#auth endpoints -> sign in and sign up
#animate endpoints -> generate matplotlib animation of the animation.md (file created and updated after every chat turn)
#get endpoints -> chat,profile


