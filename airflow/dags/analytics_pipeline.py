from airflow.sdk import dag, task

from pendulum import datetime

import sys

sys.path.append("/opt/airflow/scripts")

from run_reports import run_reports


@dag(
    dag_id="analytics_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
)

def analytics_pipeline():

    @task
    def generate_reports():

        run_reports()

    generate_reports()


analytics_pipeline()