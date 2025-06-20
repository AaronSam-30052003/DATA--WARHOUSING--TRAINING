from pathlib import Path
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

CSV_FILE = Path("/opt/airflow/dag/customers.csv")

def check_exists():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"{CSV_FILE} not found")

def count_rows():
    return sum(1 for _ in open(CSV_FILE))

def log_count(**context):
    count = context["ti"].xcom_pull(task_ids="count_rows")
    print(f"Total rows in {CSV_FILE}: {count}")
    return count

with DAG("csv_to_summary",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    t1 = PythonOperator(task_id="check_exists", python_callable=check_exists)
    t2 = PythonOperator(task_id="count_rows", python_callable=count_rows)
    t3 = PythonOperator(task_id="log_count", python_callable=log_count, provide_context=True)
    t4 = BashOperator(
        task_id="alert_if_large",
        bash_command='echo "High row count alert!"',
        trigger_rule="all_done"
    )

    t1 >> t2 >> t3 >> t4
