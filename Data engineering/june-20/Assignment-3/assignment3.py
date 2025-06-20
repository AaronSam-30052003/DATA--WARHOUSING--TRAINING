import random
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def flaky_call():
    if random.random() < 0.7:
        raise ValueError("Simulated API failure")
    print("API call success!")

def alert():
    print("All retries failed!")

with DAG("retry_with_alerts",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    t1 = PythonOperator(
        task_id="flaky_call",
        python_callable=flaky_call,
        retries=3,
        retry_delay=timedelta(minutes=1),
        retry_exponential_backoff=True
    )

    t2 = PythonOperator(task_id="alert", python_callable=alert, trigger_rule="all_failed")
    t3 = PythonOperator(task_id="on_success", python_callable=lambda: print("💚 Success!"), trigger_rule="all_success")

    t1 >> [t2, t3]
