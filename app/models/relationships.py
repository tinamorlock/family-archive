import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Relationship(Base):
    __tablename__ = 'relationship'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    person_id = Column(Integer, ForeignKey('person.id'), nullable=False) # who we're setting up the relationship for
    relative_id = Column(Integer, ForeignKey('person.id'), nullable=False) # who they are related to

    relationship_type = Column(String, nullable=False)

    person = relationship("Person", foreign_keys="relationship.person_id")
    relative = relationship("Person", foreign_keys="relationship.relative_id")