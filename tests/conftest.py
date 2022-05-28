import pytest
from sqlalchemy import create_engine
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
from sqlalchemy_utils.functions import database_exists, create_database


load_dotenv()
DB_NAME = os.environ.get("TEST_DB_NAME")
DB_USER = os.environ.get("TEST_DB_USER")
DB_PASSWORD = os.environ.get("TEST_DB_PASSWORD")
DB_HOST = os.environ.get("TEST_DB_HOST")
from src.config import Base
from src.main import app, get_db

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
)


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    if not database_exists:
        create_database(engine.url)

    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine):
    connection = db_engine.connect()

    # begin a non-ORM transaction
    transaction = connection.begin()

    # bind an individual Session to the connection
    db = Session(bind=connection)

    yield db

    db.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(db):
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c
