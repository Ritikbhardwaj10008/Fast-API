# with the help of pydantic we get request body (very important)
from pydantic import BaseModel



class Blog (BaseModel):
    title:str
    body:str
