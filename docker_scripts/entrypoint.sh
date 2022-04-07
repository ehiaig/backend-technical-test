 # entrypoint.sh
while ! pg_isready -h db -p 5432 --username=ehiaig ; do
    echo "Postgres is unavailable - sleeping"
    sleep 2
done
