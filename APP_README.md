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


### Using Kubernetes
If the APP image doesn't exists already then build it;
    - Build the Docker image: `docker build -t backend-api . -f Dockerfile`
    - Run it: `docker run -d --name backend-api-container -p 8001:8001 backend-api`
    - Tag it: `docker tag backend-api ehiaig/backend-api`
    - Then push to your remote repo: `docker push ehiaig/backend-api`. We will neeed this image later to be pulled in the Kubernetes.
- Create and apply the secrets. This will create both secret and config map to be used to connect to our db:
    `kubectl apply -f k8s/secrets.yml`
- Create postgres volume for our db:
    `kubectl apply -f k8s/postgres-volume.yml`
- Create and apply our postgres db:
    `kubectl apply -f k8s/postgres-deployment.yml`
- Then actually create the DB:
    Using:
    `kubectl exec -it postgres-7585d764d4-xzz4t -- psql -U postgres`
    OR
    Export the password:
    `export POSTGRES_PASSWORD=$(kubectl get secret postgres-secret-config -o jsonpath="{.data.password}" | base64 --decode)`
    and the create the db:
    `kubectl run postgres-client --rm --tty -i --restart=Never --image=postgres:13-alpine --env="PGPASSWORD=$POSTGRES_PASSWORD" --command -- psql -h postgres -U postgres`

    `kubectl run -it --rm --image=postgres:13-alpine postgres-client --restart=Never --command -- psql -h postgres -U postgres`
- Create and deploy backend-api
    `kubectl apply -f k8s/backendapi-deployment.yml`

Note: If you face any error, you can always debug;
    - See the state of the pod `kubectl get pods`
    - Get if a depoyment is throwing an error;
        Try to get the logs: `kubectl logs deployment/backendapi-deployment`
    - Or if you get an error about imageNeverPull, simply run `eval $(minikube docker-env)` and rebuild the docker image then.
    This command returns a set of Bash environment variable exports to configure your local environment to re-use the Docker daemon inside the Minikube instance.
