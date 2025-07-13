# with the help of pydantic we get request body (very important)
from pydantic import BaseModel
from typing import List





class BlogBase (BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    model_config = {
        "from_attributes": True
    }
    


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs :List[Blog]   # this is for the relationship ( blogs (relationship wala hai jo hmne create kia tha))
    
    model_config = {
        "from_attributes": True
    }
    
class ShowBlog(BaseModel):

    title:str
    body:str
    creator:ShowUser   # this line is for the relationshipp
    #class Config():
    #    orm_mode=True
    # the above one is for old versions the below one is new versions
    
    model_config = {
        "from_attributes": True
    }
