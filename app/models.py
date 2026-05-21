from sqlalchemy import Column,Integer,String
from database import Base

class Usercreated(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(80))
    email=Column(String(100),unique=True)
    password=Column(String(140))
