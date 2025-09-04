
from fastapi import FastAPI

app = FastAPI()

@app.get("/blog/unpublished")

def unpublished():
    return  {'data':'all unpublished blogs'}



@app.get("/blog/{id}")

def show(id:int):

    # logic to get the blog with id = id
    return  {'data':id}


@app.get("/blog/{id}/comments")
    # logic to get the comments of the blog with id = id 
def comments(id:int ):
    return {'data':{'1','2'}}
