from fastapi import FastAPI
from database import engine
from models import Base
from routes import user,task
 
 

Base.metadata.create_all(bind=engine)

app=FastAPI()


@app.get("/Home")
def home_page():
    return{
        "msg":"home page created successfully"
    }



app.include_router(user.rout)
app.include_router(task.rout)
