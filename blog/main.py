from fastapi import FastAPI , Depends  # type: ignore
from . import schemas    # type: ignore
from . import model # type: ignore 
from .database import engine , Base , SessionLocal # type: ignore
from sqlalchemy.orm import Session  # type: ignore

app=FastAPI()

model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/blog")
def create_blog(request: schemas.Blog, db:Session = Depends(get_db)): # type: ignore
    new_blog = model.Blog(title=request.title, body=request.body, author=request.author) # type: ignore
    db.add(new_blog)   
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
    
@app.get("/blog")
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(model.Blog).all()
    return blogs 
           
@app.get("/blog/{id}")
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    return blog
