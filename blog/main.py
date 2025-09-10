from fastapi import FastAPI , Depends , status, Response ,HTTPException # type: ignore
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
           
@app.get("/blog/{id}",status_code=200)
def get_blog(id: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")   
    return blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    blog.update({'title': request.title, 'body': request.body, 'author': request.author})
    db.commit()
    return "updated"