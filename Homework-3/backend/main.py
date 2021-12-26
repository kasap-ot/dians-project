import uvicorn
from fastapi import FastAPI


app = FastAPI(title="DIANS Project - Restaurant Finder")


@app.get("/", tags=["main"])
async def root():
    return {"message": "Hello world!"}