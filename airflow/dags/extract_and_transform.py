from __future__ import annotations

from airflow import DAG
from airflow.operators.bash import BashOperator
import datetime

PROJECT_PATH = "/Users/luca/Documents/CODE/DUBREU/PROJET/dataengineeringproject"

with DAG("extract_transform", start_date=datetime.datetime(2024, 1, 1),
         schedule_interval="0 * * * *", catchup=False) as dag:

    extractor = BashOperator(task_id="extractor",
                             bash_command=f"python {PROJECT_PATH}/extractor_consumer/extractor.py '2023-01-01'")

    transformer = BashOperator(task_id="transformer",
                               bash_command=f"python {PROJECT_PATH}/data_transformer/transformer.py")

    extractor >> transformer
