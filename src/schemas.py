from datetime import datetime
from src.utils import UNITS
from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class ReadingBase(BaseModel):
    patient_uuid: Optional[UUID] = None
    value: Optional[float] = None
    unit: Optional[UNITS] = "MMOL_L"
    recorded_at: Optional[datetime] = None


class ReadingCreate(ReadingBase):
    pass

class Reading(ReadingBase):
    reading_uuid: UUID

    class Config:
        orm_mode = True

class ReadingUpdate(ReadingBase):
    pass