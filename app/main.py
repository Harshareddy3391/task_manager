from fastapi import FastAPI
from database import engine
from models import Base
from routes.user import rout as user
from routes.task import Task as usertask
 

Base.metadata.create_all(bind=engine)

app=FastAPI()


@app.get("/Home")
def home_page():
    return{
        "msg":"home page created successfully"
    }



app.include_router(user)
app.include_router(usertask)
