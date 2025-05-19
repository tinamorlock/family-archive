from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RelationshipBase(BaseModel):
    person_id: int
    relative_id: int
    relationship_type: str

class RelationshipCreate(RelationshipBase):
    pass

class RelationshipRead(RelationshipBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class RelationshipUpdate(BaseModel):
    person_id: Optional[int]
    relative_id: Optional[int]
    relationship_type: Optional[str]
