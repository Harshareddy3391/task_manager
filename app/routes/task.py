from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Sesson

from sqlalchemy.ext import SQLAlchemyError
from database import SessionLocal
from models import Task
from schemas import Taskcrete

router2=APIRouter()

#database session
def get_db2():

    db2=SessionLocal()

    try:
        yield db2

    finally:
        db2.close()

#create task
@router2.post("/createtask")
def create_task(task_data:Taskcrete):

    db2=next(get_db2())
    try:
        new_task=Task(
            title=task_data.title,
              description=task_data.description,
              status=task_data.status,
              user_id=1
        )

        db2.add(new_task)
        db2.commit()
        db2.refresh(new_task)

        return {
            "message":"Task created successfully"
        }
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Data base error{str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"data base error{str(e)}"
        )
