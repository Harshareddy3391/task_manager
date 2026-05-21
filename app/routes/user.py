from fastapi import APIRouter,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from database import SessionLocal
from models import User
from schemas import Usercreate,Login
from auth import pwd_context,verify_password



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
        password=pwd_context.hash(user_info.password)

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
    

#login

@rout.post("/Login")
def user_login(user_data:Login):

    db=next(get_db())


    exist_user=db.query(User).filter(user_data.email == User.email).first()
    try:
        if not exist_user:
            raise HTTPException(
            status_code=404,
            detail="user not found"
            )
        
    
        if not verify_password(user_data.password,exist_user.password):
            raise HTTPException (
            status_code=404,
            detail="Invalid password"
            )
    

        return {
        "message":"user successfully login..."
            }
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=401,
            detail=f"internal error:{str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"somthing error{str(e)}"
        )