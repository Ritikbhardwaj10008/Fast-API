# for documentation first go to the Tutorial -User guide-> bigger application-multiple files -> then (how to add files in these routers) Import the API router 

from fastapi import APIRouter,Depends,status,HTTPException,Response
from sqlalchemy.orm import Session

# the first step is import and initialize api router
router=APIRouter(
    prefix="/blog",
    tags=['Blogs']
)


from .. import schemas,database,models
from typing import List



@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session=Depends(database.get_db)):             # here parameter is the database instance 
    blogs=db.query(models.Blog).all()           # this is how we get all the blogs
    return blogs         


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session=Depends(database.get_db)):  # request have the datatype name Blog(pydantic)
    

    new_blog=models.Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    # checking of blog is not available raise the exception
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)

    db.commit()

    return 'done'


# now to update the particular thing
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=schemas.ShowBlog)
def update(id,request:schemas.Blog,db:Session=Depends(database.get_db)):
    # this request is whatever we pass from the browser(swagger)
    blog=db.query(models.Blog).filter(models.Blog.id==id).update(request)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
    
    blog.update(request)

    db.commit()
    
    return 'updated'


# getting a particular blog with an id
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,response:Response,db:Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        response.status_code=status.HTTP_404_NOT_FOUND
        # what is this Response(this Response is form the fastAPI)
        #return {'detail':f'Blog with the {id} is not available'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the {id} is not  available')
    return blog

