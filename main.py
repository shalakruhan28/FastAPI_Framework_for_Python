
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

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


#experimenting with query parameters & sorting 
@app.get("/blog")

# define the query parameters with default values
def Blog_page(limit=10, published:bool=True, sort: str=None):
 # logic to get the blogs from the db
    if published:
        return  {'data':f'{limit} published blogs from the db'}
    else:
        return  {'data':f'{limit} blogs from the db'}

# request body
# to create a blog we need title, body, published or not
class Blog (BaseModel):
    title:str
    body:str
    published: Optional [bool]
    
# create a blog
# the data will be sent in json format
@app.post("/blog")
def create_blog(blog:Blog):
    return {'data':f'blog is created with title as {blog.title}' }
    