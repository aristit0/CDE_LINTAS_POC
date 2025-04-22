from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_create_stg():
    subprocess.run(["spark-submit", "/app/mount/employee_pipeline/scripts/create_employee_stg.py"], check=True)

def run_insert_pst():
    subprocess.run(["spark-submit", "/app/mount/employee_pipeline/scripts/insert_employee_pst.py"], check=True)

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="master_employee_dag",
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    task_create_stg = PythonOperator(
        task_id="run_create_employee_stg",
        python_callable=run_create_stg
    )

    task_insert_pst = PythonOperator(
        task_id="run_insert_employee_pst",
        python_callable=run_insert_pst
    )

    task_create_stg >> task_insert_pst