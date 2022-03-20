from sqlalchemy import (
    Column,
    BigInteger,
    DateTime,
    Enum,
    func,
    Float,
)
from src.config import Base
from sqlalchemy.orm import Session
from src.schemas import ReadingCreate
import logging
from sqlalchemy.dialects.postgresql import UUID
from src.utils import UNITS
import uuid

logger = logging.getLogger()


class Readings(Base):
    __tablename__ = "readings"

    id = Column(BigInteger, primary_key=True, index=True)
    reading_uuid = Column(UUID(as_uuid=True), default=lambda: uuid.uuid4().hex, index=True, nullable=False, unique=True)
    patient_uuid = Column(UUID(as_uuid=True), nullable=False)
    value = Column(Float, nullable=False)
    unit = Column(
        Enum(UNITS, native_enum=False),
        nullable=False,
        default=UNITS.MG_DL
    )
    recorded_at = Column(DateTime(), nullable=False)


def create_reading(db:Session, data:ReadingCreate):
    logger.info(f"Creating reading for patient: {data.patient_uuid}.")
    db_reading = Readings(
        patient_uuid=data.patient_uuid,
        value=data.value,
        unit=data.unit,
        recorded_at=data.recorded_at,
    )
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    logger.info(f"Successfully created reading for patient: {db_reading.patient_uuid}.")
    return db_reading


def all_readings(db: Session):
    return db.query(Readings).all()


def get_reading(db: Session, reading_id: uuid.UUID):
    return db.query(Readings).filter(Readings.reading_uuid == reading_id).first()
