from pydantic import BaseModel,EmailStr



class Usercreate(BaseModel):
    username:str
    email:EmailStr
    password:str

class Login(BaseModel):
      email:EmailStr
      password:str


class Taskcrete(BaseModel):
     title:str
     description:str
     status:str

     