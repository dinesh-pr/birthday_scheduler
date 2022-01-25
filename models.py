
from sqlalchemy import Column,  Integer,String,Table
from database import Base 
from sqlalchemy.sql.sqltypes import DateTime,Date

class config():
        orm_mode=True

class user(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String) 
    email=Column(String)
    password= Column(Integer)
    createdAt=Column(DateTime)
    updatedAt=Column(DateTime)

number_table=Table(
        "numbers",
        Base.metadata,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("name",String),
        Column("number",Integer),
        Column("birthday_date",Date),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime)
)

text_table=Table(
        "text",
        Base.metadata,
        Column("id",Integer,primary_key=True,autoincrement=True),
        Column("text",String),
        Column("createdAt",DateTime),
        Column("updatedAt",DateTime)
)
