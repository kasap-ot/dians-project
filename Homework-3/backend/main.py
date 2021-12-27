from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
import src.api.crud as crud
import os
from dotenv import load_dotenv


load_dotenv(".env")


app = FastAPI(title="DIANS Project - Restaurant Finder")
app.include_router(crud.router)
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DB_URL"])


@app.get("/", tags=["main"])
async def root():
    return {"message": "Hello world!"}