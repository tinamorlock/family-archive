from fastapi import FastAPI
from app.db import Base, engine
from app.routes import person

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(person.router)