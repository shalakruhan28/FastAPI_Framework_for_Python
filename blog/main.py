from fastapi import FastAPI  # type: ignore
from . import schemas # type: ignore
    
app=FastAPI()

@app.post("/blog")
def create_blog(request: schemas.Blog): # type: ignore
    return request