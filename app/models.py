from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(80))
    email=Column(String(100),unique=True)
    password=Column(String(140))


class Task(Base):
    __tablename__="task"

    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(200))
    description = Column(String(300))
    status = Column(String(50))


    user_id=Column(Integer,ForeignKey("users.id"))
    owner=relationship("User")