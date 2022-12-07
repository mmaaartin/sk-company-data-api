from fastapi import FastAPI

from .routers.v1 import company

app = FastAPI()

app.include_router(company.router)


@app.get("/")
def root():
    return {"message": "Hello to Company Data API!"}
