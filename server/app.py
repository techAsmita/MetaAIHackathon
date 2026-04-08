import os

if os.getenv("RUN_ENV") == "runner":
    exit()

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server running"}
