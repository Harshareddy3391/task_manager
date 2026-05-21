from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from database import SessionLocal
from models import User
from schemas import Usercreate



rout=APIRouter()


#database session
def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()


#register
@rout.post("/Register")
def user_register(user_info:Usercreate):
    db=next(get_db())

    try:

        new_user=User(
        username=user_info.username,
        email=user_info.email,
        password=user_info.password

        )


        db.add(new_user)
        db.commit()
        db.refresh(new_user)




        return {
        "message":"user registered successfully"
        }

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error occurred: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail="somting went wrong..."
        )