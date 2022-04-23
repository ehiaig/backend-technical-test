dir_coverage='docs/python_coverage'

mkdir -p "dir_coverage"

docker run \
    --network=backend \
    --mount type=bind, src="$(pwd)/$dir_coverage",dst=/app/htmlcov \
    backend-technical-test \
    pytests --containerized -cov=portal --cov-report=html