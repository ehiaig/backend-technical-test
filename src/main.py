from src.config import Base, SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from src.schemas import Reading, ReadingCreate, ReadingUpdate
from src.models import create_reading, all_readings, get_reading
from uuid import UUID
from typing import List
from src.errors import custom_error

Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/v1")
def welcome():
    return {"msg": "The Blood Glucose Readings API."}


@app.post("/v1/reading", response_model=Reading, status_code=201)
def create_new_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    if not hasattr(reading, "patient_uuid") or reading.patient_uuid is None:
        return custom_error(code=400, message="Invalid request")
    if not hasattr(reading, "value") or reading.value is None:
        return custom_error(code=400, message="Invalid request")
    if not hasattr(reading, "unit") or reading.unit is None:
        return custom_error(code=400, message="Invalid request")
    if not hasattr(reading, "recorded_at") or reading.recorded_at is None:
        return custom_error(code=400, message="Invalid request")
    return create_reading(db=db, data=reading)


@app.get("/v1/reading", response_model=List[Reading])
def get_all_readings(db: Session = Depends(get_db)):
    return all_readings(db)


@app.get("/v1/reading/{reading_id}", response_model=Reading, status_code=200)
def get_a_reading(reading_id: UUID, db: Session = Depends(get_db)):
    reading = get_reading(db, reading_id=reading_id)
    if reading is None:
        return custom_error(code=404, message="Reading not found")
    return reading


@app.put("/v1/reading/{reading_id}", status_code=204)
def update_a_reading(reading_id: UUID, reading_data: ReadingUpdate, db: Session = Depends(get_db)):
    db_reading = get_reading(db, reading_id=reading_id)
    if db_reading is None:
        return custom_error(code=404, message="Reading not found")
    if hasattr(reading_data, "patient_uuid") and reading_data.patient_uuid is not None:
        db_reading.patient_uuid = reading_data.patient_uuid
    if hasattr(reading_data, "value") and reading_data.value is not None:
        db_reading.value = reading_data.value
    if hasattr(reading_data, "unit") and reading_data.unit is not None:
        db_reading.unit = reading_data.unit
    if hasattr(reading_data, "recorded_at") and reading_data.recorded_at is not None:
        db_reading.recorded_at = reading_data.recorded_at
    db.commit()
    db.refresh(db_reading)
    return "Reading updated successfully"


@app.delete("/v1/reading/{reading_id}", status_code=204)
def delete_a_reading(reading_id: UUID, db: Session = Depends(get_db)):
    reading = get_reading(db, reading_id=reading_id)
    if reading is None:
        return custom_error(code=404, message="Reading not found")
    db.delete(reading)
    db.commit()
    return "Reading deleted successfully"
