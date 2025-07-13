from fastapi import FastAPI,Depends,status,Response,HTTPException


from blog import schemas, models
from blog.database import engine ,SessionLocal # we write like this bcz the thing we are inprting here is not a function
from sqlalchemy.orm import Session
from typing import List
from .hashing import Hash


app=FastAPI()


models.Base.metadata.create_all(engine)  # this is the reason of creation of table (here we need to provide a database engine)
# this line is extremely important.(whenerver we are running hte server we are going to create all the modelsin the database(we can simply say migrating all the tables.))
# if table is present it is not doing anything,but if the table is not there it is going to create it.


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
# post request (to store the blog infromation into our database.)

@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
def create(request:schemas.Blog,db:Session=Depends(get_db)):  # request have the datatype name Blog(pydantic)
    # What we did -> we define the db(db should be the instance or type of session but session is sqlorm part ,so we have to add the default value which is depends on the db)
    # now db instance is  created
    # now the new blog is going to be the blog model-> model refers to the db structure (models.py)
    # in this we tell what is title, what is the body 
    # then add 
    # commit 
    # referesh

    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

# we need to store all the request body into the database

# get request to see all the blogs
@app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
def all(db:Session=Depends(get_db)):             # here parameter is the database instance 
    blogs=db.query(models.Blog).all()           # this is how we get all the blogs
    return blogs         

    
# getting a particular blog with an id
@app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['blogs'])
def show(id,response:Response,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        response.status_code=status.HTTP_404_NOT_FOUND
        # what is this Response(this Response is form the fastAPI)
        #return {'detail':f'Blog with the {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the {id} is not  available')
    return blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def destroy(id,db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    # checking of blog is not available raise the exception
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)

    db.commit()

    return 'done'
    # how do we delete anything from the sql alchemy

#    ✅ How SQLAlchemy works:
#    You want to...	           You write
#    Get all rows	           db.query(Model).all()
#    Filter rows	           db.query(Model).filter(...).all()
#    Delete rows	           db.query(Model).filter(...).delete()
#    Add a new row	           db.add(obj)


# now to update the particular thing
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.ShowBlog,tags=['blogs'])
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    # this request is whatever we pass from the browser(swagger)
    blog=db.query(models.Blog).filter(models.Blog.id==id).update(request)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    
    blog.update(request)

    db.commit()
    
    return 'updated'







@app.post('/user',response_model=schemas.ShowUser,tags=['users'])
def create_user(request:schemas.User,db:Session=Depends(get_db)):
   
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
def get_user(id:int ,db: Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user




# python -m blog.main  run this file like this 