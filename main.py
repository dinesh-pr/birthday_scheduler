from distutils.command.upload import upload
from fastapi import FastAPI
from routers import opration,register,upload,get_data,text
import models
from database import engine

app=FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(register.router)
app.include_router(opration.router)
app.include_router(upload.router)
app.include_router(get_data.router)
app.include_router(text.router)


