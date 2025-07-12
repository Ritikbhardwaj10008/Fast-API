# with the help of pydantic we get request body (very important)
from pydantic import BaseModel






class Blog (BaseModel):
    title:str
    body:str


class ShowBlog(BaseModel):

    title:str
    body:str

    #class Config():
    #    orm_mode=True
    # the above one is for old versions the below one is new versions
    model_config = {
        "from_attributes": True
    }


class User(BaseModel):
    name:str
    email:str
    password:str