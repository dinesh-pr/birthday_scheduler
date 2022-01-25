
from datetime import datetime
from sqlalchemy import  select,insert
from fastapi import APIRouter, File, UploadFile,Depends
from sqlalchemy.orm import Session
from io import StringIO
from models import number_table
import pandas as pd
from database import get_db
router= APIRouter(
	tags=["uploadfile"]
)
@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...),db:Session=Depends(get_db)):
        data=pd.read_csv(StringIO(str(file.file.read(), "UTF-8")), encoding="UTF-8")
        for index in range(len(data.index)):
                name=f'{data.iloc[index][0]}{data.iloc[index][1]}'
                num=str(data.iloc[index][2])
                number=data.iloc[index][3]
                d = datetime.strptime(number, '%Y-%m-%d').date()
                new=db.execute(number_table.insert().values(
                                name=name,
                                number=num,
                                createdAt=datetime.date(),
                                birthday_date=d
                                        )
                                )
                db.commit()
        return "comleted"