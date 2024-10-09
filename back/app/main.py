from fastapi import FastAPI
from app.api import endpoints

app = FastAPI()

app.include_router(endpoints.router)

@app.get("/")
async def root():
    return {"message": "API is running"}
