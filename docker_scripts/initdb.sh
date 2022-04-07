#!/bin/bash

POSTGRES_USER=ehiaig
POSTGRES_PASSWORD=password
POSTGRES_PORT=5432
POSTGRES_HOST=localhost
POSTGRES_DB=reading_db
TEST_DB_PASSWORD=reading_db_test

psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'reading_db2'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE reading_db2"
echo "reading_db check is completed"
psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'reading_db_test'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE reading_db_test"
echo "reading_db_test check is completed"