from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "depends_on_past": False,
    "retries": 0
}

with DAG("master_employee_dag",
         default_args=default_args,
         schedule_interval=None,
         catchup=False,
         description="DAG to run create STG and insert PST employee Iceberg jobs") as dag:

    create_stg = SparkSubmitOperator(
        task_id="create_employee_stg",
        application="/app/mount/employee_pipeline/scripts/create_employee_stg.py",
        conn_id="spark_default"
    )

    insert_pst = SparkSubmitOperator(
        task_id="insert_employee_pst",
        application="/app/mount/employee_pipeline/scripts/insert_employee_pst.py",
        conn_id="spark_default"
    )

    create_stg >> insert_pst