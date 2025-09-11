from .database import Base  # type: ignore
from sqlalchemy import Column, Integer, String  # type: ignore


class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    author = Column(String, index=True)

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String,  index=True)
    password = Column(String)
    