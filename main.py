
from fastapi import FastAPI

app = FastAPI()


@app.get("/about")

def about():
    return  {'data':{'about page'}}


@app.get("/")

def index():
    return {'data':{'name':'hello world'}}
