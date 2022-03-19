from src.config import Base, SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from src.schemas import Reading, ReadingCreate
from src.models import create_reading
from uuid import UUID

Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def welcome():
    return {"msg": "The Blood Glucose Readings API."}


@app.post("/v1/reading", response_model=Reading, status_code=201)
def create_new_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    return create_reading(db=db, data=reading)
