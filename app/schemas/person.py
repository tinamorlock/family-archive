from pydantic import BaseModel
from datetime import date
from typing import Optional

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[date]
    death_date: Optional[date]
    gender: Optional[str]
    notes: Optional[str]

class PersonCreate(PersonBase):
    pass

class Person(PersonBase):
    id: int
    photo_path: Optional[str]

    class Config:
        orm_mode = True