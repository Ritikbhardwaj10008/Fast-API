from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app=FastAPI()  # creating the instance of the app

@app.get('/')
def index():
    return {'data':'blog list'}

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    
    # only get 10 published blogs (we need published for true false thing)
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit} blogs from the db'}
    



@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    # fetch blog with id =id
    return {'data':id}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}
 
@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments
    return {'data':{'1','2'}}



class Blog(BaseModel):
    title:str 
    body:str
    published: Optional[bool]


@app.post('/blog')
def createblog(blog:Blog):
    
    return {'data':f"blog is created with title as {blog.title}"}
