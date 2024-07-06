from backend.database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
from backend.parser import *

# создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()


# определяем зависимость
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse("frontend/index.html")


@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    return db.query(Vac).all()



@app.post("/api/users")
def create_person(db: Session = Depends(get_db), data  = Body()):
    get_vacancies(db, keyword=data["keyword"], graphic=data["graphic"], experience=data["experience"], emp=data["emp"], field=data["field"], page=data["page"] )




