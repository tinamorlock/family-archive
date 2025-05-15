from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Date
from app.db import Base

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=True)
    death_date = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    photo_path = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
