## RUNNING THE APP
### Using the Makefile:
- Generate a `.env` file using the command below:
    ```
    cp .env.example .env
    ```
    Update the contents with the approritate values
- Export those values:
    ```
    export DB_NAME=reading_db
    export DB_USER=ehi
    export DB_PASSWORD=password 
    export DB_SERVER=localhost 
    export TEST_DB_NAME=reading_db_test 
    export TEST_DB_USER=ehi 
    export TEST_DB_PASSWORD=password 
    export TEST_DB_SERVER=localhost
    ```
- Install Poetry on your computer from here https://python-poetry.org/docs/. Then install the app dependencies using: `make install`
- Create the specified `reading_db` and `reading_db_test` databases using: `make db`
- Run the app using: `make run`
- Run the tests using: `make test`


### Using Docker
#### Setup a Postgress Database in Docker
- Start Postgres database with the command below:
    ```
    docker run --name readingdbcontainer -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
    ```
- Create the `reading_db` database by running the command below:
    ```
    python3 scripts/create_db.py --dbname reading_db --dbuser ehi --dbpassword password --dbhost localhost --dbport 5432
    ```

#### Build and run the app in Docker
- Build the Docker image:
    ```
    docker build -t backendapp . -f Dockerfile
    ```

- Run the image you just built as a container, parsing in the necessary environment variables that the app needs as specified in the `.env` file.
    ```
    docker run -d --name backendappcontainer -p 8000:8000 -e DB_NAME=reading_db -e DB_USER=ehi -e DB_PASSWORD=password -e DB_SERVER=host.docker.internal  backendapp
    ```
