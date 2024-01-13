from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task
from airflow.decorators.python import PythonOperator
import datetime

with DAG(dag_id="test", start_date=datetime.datetime.today(), schedule_interval="@hourly"):
    hello = BashOperator(task_id="hello", bash_command="echo hello")


    def call_me():
        print("hey i juste met and this is crazy")
        return 2


    step2 = PythonOperator(task_id="step2", python_callable=call_me)

    hello >> step2
