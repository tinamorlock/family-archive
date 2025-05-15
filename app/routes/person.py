from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.person import Person, PersonCreate
from app.crud.person import create_person, get_people
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/person/", response_model=Person)
def create_new_person(person: PersonCreate, db: Session = Depends(get_db)):
    return create_person(db=db, person=person)

@router.get("/person/", response_model=list[Person])
def read_person(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_people(skip=skip, limit=limit, db=db)