from pathlib import Path
from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

FILE = Path("/opt/airflow/dags/inventory.csv")

def choose_path():
    size = FILE.stat().st_size
    return "light_summary" if size < 500 * 1024 else "detailed_processing"

def light_summary():
    print("Running light summary")

def detailed_processing():
    print("Running detailed processing")

with DAG("branch_by_size",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    branch = BranchPythonOperator(task_id="branch_choice", python_callable=choose_path)
    tA = PythonOperator(task_id="light_summary", python_callable=light_summary)
    tB = PythonOperator(task_id="detailed_processing", python_callable=detailed_processing)
    cleanup = BashOperator(task_id="cleanup", bash_command="echo 'Cleaning up...'")

    branch >> [tA, tB] >> cleanup
