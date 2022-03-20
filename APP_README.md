## Running the APP
From the `backend-technical-test` repo:
### Without Docker
- Generate a `.env` file using the command below:
    ```
    cp .env.example .env
    ```
- Create the `reading_db` database by running the command below:
    ```
    python3 scripts/create_db.py --dbname reading_db --dbuser obama --dbpassword password --dbhost localhost --dbport 5432
    ```
    Replace `obama` and `password` with the right user and password.
- Run `pip3 install -r requirements.txt`
- Run the app:
    ```
    uvicorn src.main:app --reload
    ```

### With Docker
#### Setup a Postgress Database in Docker
- Start Postgres database with the command below:
    ```
    docker run --name readingdbcontainer -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
    ```
- Create the `reading_db` database by running the command below:
    ```
    python3 scripts/create_db.py --dbname reading_db --dbuser obama --dbpassword password --dbhost localhost --dbport 5432
    ```

#### Build and run the app in Docker
- Build the Docker image:
    ```
    docker build -t backendapp . -f Dockerfile
    ```

- Run the image you just built as a container, parsing in the necessary environment variables that the app needs as specified in the `.env` file.
    ```
    docker run -d --name backendappcontainer -p 8000:8000 -e DB_NAME=reading_db -e DB_USER=obama -e DB_PASSWORD=password -e DB_SERVER=host.docker.internal  backendapp
    ```