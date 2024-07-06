from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String



from fastapi import FastAPI

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase): pass


class Vac(Base):
    __tablename__ = "vac"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    graphic = Column(String)
    experience = Column(String)
    emp = Column(String)
    company = Column(String)
    URL = Column(String)




SessionLocal = sessionmaker(autoflush=False, bind=engine)