import shutil
import pandas as pd
from pathlib import Path
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

INPUT = Path("/opt/airflow/dags/sales.csv")
SUMMARY = Path("/opt/airflow/dags/sales_summary.csv")
ARCHIVE = Path("/opt/airflow/dags/archive/")

default_args = {
    "execution_timeout": timedelta(minutes=5)
}

def process_sales():
    df = pd.read_csv(INPUT)
    summary = df.groupby("category")["amount"].sum().reset_index()
    summary.to_csv(SUMMARY, index=False)
    print("Sales summary created.")


def archive_file():
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    shutil.move(str(INPUT), str(ARCHIVE / INPUT.name))
    print(f"Archived to {ARCHIVE}")


with DAG(
    dag_id="daily_sales_report",
    start_date=datetime(2025, 1, 1),
    schedule_interval="0 6 * * *",  # Every day at 6 AM
    catchup=False,
    default_args=default_args,
    tags=["assignment2"]
) as dag:

    task_process = PythonOperator(
        task_id="process_sales",
        python_callable=process_sales
    )

    task_archive = PythonOperator(
        task_id="archive_file",
        python_callable=archive_file
    )

    task_process >> task_archive
