from fastapi import FastAPI
import src.api.crud as crud


app = FastAPI(title="DIANS Project - Restaurant Finder")
app.include_router(crud.router)


@app.get("/", tags=["main"])
async def root():
    return {"message": "Hello world!"}