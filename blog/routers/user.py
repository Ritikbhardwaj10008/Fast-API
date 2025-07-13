from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from ..hashing import Hash

router=APIRouter(
    prefix="/user",
    tags=['Users']
)
# how router help us in minimising the code -> we assingn tags here only we dont need to give tags to every body in their @path
# one more thing is prefixing we can prefix all the routes with some names

from .. import schemas,database,models
from typing import List


@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):
   
    new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user



@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int ,db: Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user

