from fastapi import FastAPI , Depends , status, Response ,HTTPException # type: ignore
from . import schemas    # type: ignore
from . import model # type: ignore 
from .database import engine , Base , SessionLocal # type: ignore
from sqlalchemy.orm import Session  # type: ignore
from typing import List  # type: ignore
from .hashing import Hash  # type: ignore


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
    
    
@app.get("/blog",response_model=list[schemas.ShowBlog], status_code=200)
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

@app.post("/user", response_model=schemas.ShowUser)
def creat_user(request: schemas.User, db:Session = Depends(get_db)): # type: ignore
    
    
    new_user = model.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password )) # type: ignore
    db.add(new_user)    
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/user/{id}",response_model=schemas.ShowUser, status_code=200)
def get_users(id:int,db: Session = Depends(get_db)):
    user = db.query(model.User).filter(model.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found") 
    return user     # pyright: ignore[reportUndefinedVariable]