PYTHON = python3
DBUSER = obama
DBPASSWORD = password

all: two

create_db:
	python3 scripts/create_db.py --dbname reading_db --dbuser ${DBUSER} --dbpassword ${DBPASSWORD} --dbhost localhost --dbport 5432

tests:
	pytest tests/test_main.py
	# ${PYTHON} -m pytest

install:
	poetry install

run:
	uvicorn src.main:app --reload

clean:
	rm -r *.project