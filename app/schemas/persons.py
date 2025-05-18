import datetime
from typing import Optional

from pydantic import BaseModel

class PersonBase(BaseModel):
    fname: str
    lname: str
    date_of_birth: Optional[datetime] = None
    date_of_death: Optional[datetime] = None
    city_of_birth: Optional[str] = None
    state_of_birth: Optional[str] = None
    country_of_birth: Optional[str] = None
    city_of_death: Optional[str] = None
    state_of_death: Optional[str] = None
    country_of_death: Optional[str] = None
    cause_of_death: Optional[str] = None
    owner_id: int

class PersonCreate(PersonBase):
    pass

class PersonUpdate(PersonBase):
    fname: Optional[str] = None
    lname: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    date_of_death: Optional[datetime] = None
    city_of_birth: Optional[str] = None
    state_of_birth: Optional[str] = None
    country_of_birth: Optional[str] = None
    city_of_death: Optional[str] = None
    state_of_death: Optional[str] = None
    country_of_death: Optional[str] = None
    cause_of_death: Optional[str] = None

class PersonRead(PersonBase):
    id: int
    fname: str
    lname: str
    date_of_birth: Optional[datetime] = None
    date_of_death: Optional[datetime] = None
    city_of_birth: Optional[str] = None
    state_of_birth: Optional[str] = None
    country_of_birth: Optional[str] = None
    city_of_death: Optional[str] = None
    state_of_death: Optional[str] = None
    country_of_death: Optional[str] = None
    cause_of_death: Optional[str] = None
    owner_id: int

    class Config:
        orm_mode = True