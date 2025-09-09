from .database import Base  # type: ignore
from sqlalchemy import Column, Integer, String  # type: ignore


class Blog(Base):
    __tablename__ = "Blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    author = Column(String, index=True)
