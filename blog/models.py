# pip install sqlalchemy
from sqlalchemy import Column,Integer,String,Text
from sqlalchemy.orm import Mapped, mapped_column
#from blog.database import Base  # this base is from the database  (an object of declarative base)


#When you create models using SQLAlchemy, you’re not just writing Python classes — you’re defining database table structure, column types, primary keys, foreign keys, etc.
#But Python doesn’t understand SQL. So SQLAlchemy needs:
#A registry to track what class corresponds to what table
#A metadata object to hold all the table definitions
#A way to auto-generate SQL from your classes
#This “registry + metadata + mapping system” is what you get from a base class, which in SQLAlchemy 2.0 is created like this:
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
##########################################################################
class Blog(Base):  #model this is inherited to base , and then we create the table here(Blog is extended base of the database)
    __tablename__ = 'blogs'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    body: Mapped[str] = mapped_column(Text)
    
 
