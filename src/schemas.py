from datetime import datetime
from src.utils import UNITS
from pydantic import BaseModel
from uuid import UUID


class ReadingBase(BaseModel):
    patient_uuid: UUID
    value: float
    unit: UNITS
    recorded_at: datetime


class ReadingCreate(ReadingBase):
    pass

class Reading(ReadingBase):
    reading_uuid: UUID

    class Config:
        orm_mode = True

class ReadingUpdate(ReadingBase):
    pass