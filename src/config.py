from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
)

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
import time

engine = None
SessionLocal = None
Base = None

retries = 5
while retries > 0:
    try:
        engine = create_engine(
            SQLALCHEMY_DATABASE_URL
        )
        SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
        print("DB Connected")
        break
    except Exception as e:
        print("Error connecting..." + str(e))
        retries -= 1
        time.sleep(3)