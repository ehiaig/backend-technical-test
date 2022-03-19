from src.config import Base, SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from src.schemas import Reading, ReadingCreate, ReadingUpdate
from src.models import create_reading, all_readings, get_reading
from uuid import UUID
from typing import List
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

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


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.post("/v1/reading", response_model=Reading, status_code=201)
def create_new_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    return create_reading(db=db, data=reading)

@app.get("/v1/reading", response_model=List[Reading])
def get_all_readings(db: Session = Depends(get_db)):
    return all_readings(db)


@app.get("/v1/reading/{reading_id}", response_model=Reading, status_code=200)
def get_a_reading(reading_id: UUID, db: Session = Depends(get_db)):
    reading = get_reading(db, reading_id=reading_id)
    if reading is None:
        raise HTTPException(
            status_code=404, detail="Reading not found"
        )
    return reading


@app.put("/v1/reading/{reading_id}", status_code=204)
def update_a_reading(reading_id: UUID, reading_data: ReadingUpdate, db: Session = Depends(get_db)):
    db_reading = get_reading(db, reading_id=reading_id)
    if db_reading is None:
        raise HTTPException(
            status_code=404, detail="Reading not found"
        )
    db_reading.patient_uuid = reading_data.patient_uuid
    db_reading.value = reading_data.value
    db_reading.unit = reading_data.unit
    db_reading.recorded_at = reading_data.recorded_at
    db.commit()
    return "Reading updated successfully"


@app.delete("/v1/reading/{reading_id}", status_code=204)
def delete_a_reading(reading_id: UUID, db: Session = Depends(get_db)):
    reading = get_reading(db, reading_id=reading_id)
    if reading is None:
        raise HTTPException(
            status_code=404, detail="Reading not found"
        )
    db.delete(reading)
    db.commit()
    return "Reading deleted successfully"