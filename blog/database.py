from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#SQLALCHAMY_DATABASE_URL='sqlite+pysqlite:///./blog.db'
SQLALCHAMY_DATABASE_URL = "mysql+pymysql://root:@localhost/blogg"

#engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={'check_same_thread':False})
#above line is for sqlite
#below is for pymsql
engine = create_engine(SQLALCHAMY_DATABASE_URL)


SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
# Declare mapping
#Base=declarative_base()   # this base is inherited in the models.py 
# now this way is not required in sqlalchemy2.0





def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()