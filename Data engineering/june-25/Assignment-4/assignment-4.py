import time
import random
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def long_task():
    duration = random.randint(1,10)
    print(f"Sleeping {duration}s")
    time.sleep(duration)
    if duration > 8:
        raise RuntimeError("Took too long!")

def on_success(): print("Success")
def on_failure(): print("Failed after retries")

with DAG("retry_timeout_dag",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    t = PythonOperator(
        task_id="long_task",
        python_callable=long_task,
        retries=2,
        retry_delay=timedelta(seconds=10),
        retry_exponential_backoff=True,
        execution_timeout=timedelta(seconds=5)
    )
    ts = PythonOperator(task_id="on_success", python_callable=on_success, trigger_rule="all_success")
    tf = PythonOperator(task_id="on_failure", python_callable=on_failure, trigger_rule="all_failed")

    t >> [ts, tf]
