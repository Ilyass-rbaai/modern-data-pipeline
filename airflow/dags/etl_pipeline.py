from datetime import datetime

from airflow.sdk import dag, task

import sys
import os


sys.path.append("/opt/airflow/scripts")

from extract import extract
from validate import validate
from transform import transform
from load import load
from report import run_reports


@dag(
    dag_id="modern_etl_pipeline",

    start_date=datetime(2026, 8, 1),

    schedule="@daily",

    catchup=False,

    tags=["etl", "postgres", "portfolio"],
)

def modern_etl_pipeline():

    @task
    def extract_task():

        return extract()

    @task
    def validate_task(datasets):

        return validate(datasets)

    @task
    def transform_task(datasets):

        return transform(datasets)

    @task
    def load_task(datasets):

        load(datasets)

    @task
    def report_task():

        run_reports()

    extracted = extract_task()

    validated = validate_task(extracted)

    transformed = transform_task(validated)

    loaded = load_task(transformed)

    reports = report_task()

    loaded >> reports


modern_etl_pipeline()