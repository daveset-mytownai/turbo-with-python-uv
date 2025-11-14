from fastapi import FastAPI
from python_lib import greet

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Python FastAPI app (version 2 - no package)!"}


@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": greet(name)}
