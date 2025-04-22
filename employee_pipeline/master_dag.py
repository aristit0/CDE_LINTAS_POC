from airflow import DAG
from datetime import datetime
from cloudera.cde.operators.cde_operator import CDEJobRunOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
    "depends_on_past": False,
}

with DAG("master_employee_dag",
         default_args=default_args,
         schedule_interval=None,
         catchup=False,
         description="Run staging and partition insert jobs") as dag:

    create_stg = CDEJobRunOperator(
        task_id="create_employee_stg",
        name="create-employee-stg",  # nama job di CDE
    )

    insert_pst = CDEJobRunOperator(
        task_id="insert_employee_pst",
        name="insert-employee-pst",  # nama job di CDE
    )

    create_stg >> insert_pst