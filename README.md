# Data Investigation Platform

This repository contains a lightweight prototype of a Data Investigation Platform inspired by the detailed design.

## Setup

Install dependencies using `poetry` and run the Flask application:

```bash
poetry install
FLASK_APP=app.main flask run --reload
```

To start the Airflow scheduler and webserver (after initialization):

```bash
poetry run airflow db init
poetry run airflow users create \
    --username admin --firstname Admin --lastname User \
    --role Admin --email admin@example.com --password admin
poetry run airflow scheduler &
poetry run airflow webserver -p 8080 &
```

The sample DAG in `dags/investigation_dag.py` demonstrates automated
investigation tasks.

### Frontend Development

A minimal React application lives in `frontend/`. Install Node dependencies and start the development server with:

```bash
cd frontend
npm install
npm run dev
```

The dev server proxies API requests to the Flask backend.


### Distributed Processing

This prototype includes simple wrappers for executing SQL on Hive via
Spark and consuming streaming data with Flink. See `src/app/services/spark.py`
and `src/app/services/flink.py` for details.

### Security and Permissions

The `permissions` service exposes a pluggable interface so you can
provide your own authorization logic. By default a very small role
matrix is included. Investigation data is stored encrypted using a
Fernet key from the `cryptography` package. When results are returned
to clients a watermark based on the requesting user's identifier is
embedded for traceability.

Blockchain can be integrated at the audit-log layer if stricter
immutability is required, but the prototype does not implement it.

Run tests with:

```bash
pytest
```
