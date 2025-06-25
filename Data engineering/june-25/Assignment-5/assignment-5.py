from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator

def choose_task():
    now = datetime.now().time()
    if now.hour < 12:
        return "morning_task"
    elif now.hour < 18:
        return "afternoon_task"
    else:
        return "cleanup"

def morning(): print("Good morning!")
def afternoon(): print("Good afternoon!")

with DAG("time_based_branching",
         start_date=datetime(2025,1,1),
         schedule_interval="0 * * * *",
         catchup=False) as dag:

    branch = BranchPythonOperator(task_id="branch", python_callable=choose_task)
    m = PythonOperator(task_id="morning_task", python_callable=morning)
    a = PythonOperator(task_id="afternoon_task", python_callable=afternoon)
    cleanup = DummyOperator(task_id="cleanup")

    branch >> [m, a, cleanup] >> cleanup
