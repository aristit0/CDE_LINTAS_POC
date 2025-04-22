from datetime import datetime, timedelta
from airflow import DAG
from cloudera.airflow.providers.operators.cde import CdeRunJobOperator

default_args = {
    'owner': 'airflow',
    'retry_delay': timedelta(seconds=10),
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='master_employee_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    is_paused_upon_creation=False
) as dag:

    create_stg_task = CdeRunJobOperator(
        task_id='create_stg',
        job_name='create-employee-stg',  # Sesuai job yang kamu buat di CDE
        connection_id='Default-VC-xgxksvr8'      # atau 'cde-vc01-dev' kalau itu VC kamu
    )

    insert_pst_task = CdeRunJobOperator(
        task_id='insert_pst',
        job_name='insert-employee-pst'
    )

    create_stg_task >> insert_pst_task