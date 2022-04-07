PYTHON = python3

MAIN_DB_NAME = ${DB_NAME}
MAIN_DB_USER = ${DB_USER}
MAIN_DB_PASSWORD = ${DB_PASSWORD}
MAIN_DB_HOST = ${DB_HOST}
TEST_DB_NAME = ${TEST_DB_NAME}
TEST_DB_USER = ${TEST_DB_USER}
TEST_DB_PASSWORD = ${TEST_DB_PASSWORD}
TEST_DB_HOST = ${TEST_DB_HOST}

db:
	python3 scripts/create_db.py --dbname ${MAIN_DB_NAME} --dbuser ${MAIN_DB_USER} --dbpassword ${MAIN_DB_PASSWORD} --dbhost ${MAIN_DB_HOST} --dbport 5432
	python3 scripts/create_db.py --dbname ${TEST_DB_NAME} --dbuser ${TEST_DB_USER} --dbpassword ${TEST_DB_PASSWORD} --dbhost ${TEST_DB_HOST} --dbport 5432

test:
	${PYTHON} -m pytest

install:
	poetry install

run:
	uvicorn src.main:app --reload
