from airflow import DAG
from datetime import datetime
from cloudera.cde.operators.cde_operator import CDEJobRunOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="master_employee_dag",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description="Run staging and partition insert jobs via CDE Spark Jobs"
) as dag:

    run_create_stg = CDEJobRunOperator(
        task_id="create_employee_stg",
        name="create-employee-stg"
    )

    run_insert_pst = CDEJobRunOperator(
        task_id="insert_employee_pst",
        name="insert-employee-pst"
    )

    run_create_stg >> run_insert_pst