
from datetime import datetime
from pydoc import text
from fastapi import APIRouter,Depends,Response,status,HTTPException
from numpy import not_equal
from pandas import notnull
from sqlalchemy.orm import Session
from database import get_db 
import re
from sqlalchemy import Table, null
from models import text_table,number_table
import schemas,models

router=APIRouter(
    tags=["text"]
)

@router.post("/text")
def add_text(resoponce:Response,request:schemas.text,db:Session=Depends(get_db)):
    t=request.text
    try:
        te=re.search(r"\[([A-Za-z]+)\]", t)
        m=te.group(1)
        if (m!= null):
                new_text=db.execute(text_table.insert().values(text=t,createdAt=datetime.now()))
                db.commit()
                return "added "
    except:
        return "please enter valid name"

@router.get("/text")
def get_text(db:Session=Depends(get_db)):
    new_text=db.execute(text_table.select().with_only_columns([text_table.c.text])).fetchall()
    return new_text

@router.post("/text/update")
def update_text(id,request:schemas.text,db:Session=Depends(get_db)):
    new_text=db.query(models.text_table).filter(text_table.c.id==id)
    if not new_text.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"text with {id} not here")
    t=request.text
    try:
        te=re.search(r"\[([A-Za-z]+)\]", t)
        m=te.group(1)
        if (m!= null):
                new_text=db.execute(text_table.update(text_table.c.id==id).values(text=t,createdAt=datetime.now()))
                db.commit()
                return "added "
    except:
        return "please enter valid name"
    