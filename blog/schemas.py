from pydantic import BaseModel  # type: ignore


class Blog(BaseModel):
    title:str
    body:str
    author:str
    
class ShowBlog(BaseModel):
    title:str
    body:str    
    class config ():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str
    