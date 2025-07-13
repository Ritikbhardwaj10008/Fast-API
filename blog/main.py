from fastapi import FastAPI


from blog import  models
from blog.database import engine  # we write like this bcz the thing we are inprting here is not a function
from .routers import blog   # this is for include_routers.
from .routers import user


app=FastAPI()


models.Base.metadata.create_all(engine)  # this is the reason of creation of table (here we need to provide a database engine)
# this line is extremely important.(whenerver we are running hte server we are going to create all the modelsin the database(we can simply say migrating all the tables.))
# if table is present it is not doing anything,but if the table is not there it is going to create it.


# we have to include the router and define whatever the router we want to give(in this we are giving the router present in blog)




# we need to store all the request body into the database

app.include_router(blog.router) # we need to include the router her in the main file.
# get request to see all the blogs
#@app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
#def all(db:Session=Depends(get_db)):             # here parameter is the database instance 
#    blogs=db.query(models.Blog).all()           # this is how we get all the blogs
#    return blogs         

    



    # how do we delete anything from the sql alchemy

#    ✅ How SQLAlchemy works:
#    You want to...	           You write
#    Get all rows	           db.query(Model).all()
#    Filter rows	           db.query(Model).filter(...).all()
#    Delete rows	           db.query(Model).filter(...).delete()
#    Add a new row	           db.add(obj)


app.include_router(user.router)













# python -m blog.main  run this file like this 