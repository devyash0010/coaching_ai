from fastapi import FastAPI

from routes import router



app=FastAPI(

    title="Coaching AI Backend",

    version="1.0"

)



app.include_router(router)

@app.get("/")

def home():

    return {

        "message": "Coaching AI Backend Running"

    }