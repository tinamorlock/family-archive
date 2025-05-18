import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    fname = Column(String, nullable=False)
    lname = Column(String, nullable=False)
    date_of_birth = Column(DateTime)
    date_of_death = Column(DateTime)
    city_of_birth = Column(String)
    state_of_birth = Column(String)
    country_of_birth = Column(String)
    city_of_death = Column(String)
    state_of_death = Column(String)
    country_of_death = Column(String)
    cause_of_death = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    owner_id = Column(Integer) # no FK set due to abstraction