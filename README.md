Intro: This is a simple back-end service for managing the blood glucose readings of diabetes patients. Read more about it [here][https://github.com/ehiaig/backend-technical-test/TASK.md].  
## RUNNING THE APP
Initial setup:
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
    export DB_HOST=localhost 
    export TEST_DB_NAME=reading_db_test 
    export TEST_DB_USER=ehi 
    export TEST_DB_PASSWORD=password 
    export TEST_DB_HOST=localhost
    ```
- Options to run:
    - via [makefile](#using-the-Makefile)
    - via [docker](#using-docker)
    - via [docker-compose](#using-docker-compose)
### Using the Makefile:
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
    docker run -d --name backendappcontainer -p 8000:8000 -e DB_NAME=reading_db -e DB_USER=ehi -e DB_PASSWORD=password -e DB_HOST=host.docker.internal  backendapp
    ```


### Using Docker Compose
    - Run the images: `docker-compose up -d`
    - Confirm the containers are running: `docker ps`
    - Visit the app in your browser `localhost:8000/docs

    Notes: 
    - If you try to load app in the browser and it fails;
        - Get the api container id: `docker ps`
        - Check it's logs: `docker logs -f 72a2a610baf3`
    - If the errors like `... TCP/IP connections on port 5432?` it may be that  another postgresql running over your localhost causing this one to fail.
        - destroy the built container: `docker-compose down`
        - Run `docker rmi -f $(docker images -a -q)` to clear cached postgres data
        - The rebuild the image `docker-compose up -d`
        - isit the app in your browser `localhost:8000/docs

