from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def start_investigation():
    print("Starting automated investigation")


def finish_investigation():
    print("Investigation complete")


default_args = {
    "start_date": datetime(2024, 1, 1),
    "catchup": False,
}

with DAG(
    "investigation_dag",
    schedule_interval="@daily",
    default_args=default_args,
    tags=["investigation"],
) as dag:

    start = PythonOperator(task_id="start", python_callable=start_investigation)
    end = PythonOperator(task_id="finish", python_callable=finish_investigation)

    start >> end
