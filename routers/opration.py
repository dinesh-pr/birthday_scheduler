from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import get_db

import schemas
import models
from models import number_table

router=APIRouter(tags=['operation'] )

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    number=db.execute(number_table.select().where(number_table.c.id==id)).first()
    if not number:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with {id} not here")
    db.execute(number_table.delete().where(number_table.c.id==id))
    db.commit()
    return "deteted"

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.update,db:Session=Depends(get_db)):
    blog=db.query(models.number_table).filter(number_table.c.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with {id} not here")
    blog.update(request.dict())
    db.commit()
    return "updated"


