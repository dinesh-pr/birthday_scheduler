from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from models import number_table
router=APIRouter(
    tags=["getdata"]
)

@router.get("/{page_no}/{no_of_data}")
def get(no_of_data:int,page_no:int,db:Session=Depends(get_db)):
    data=db.execute(number_table.select().limit(no_of_data).offset(page_no*50)).fetchall()
    return data
