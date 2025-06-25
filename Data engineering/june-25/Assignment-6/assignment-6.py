from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.email import EmailOperator

def task_1(): pass
def task_2(): pass

with DAG("email_notification",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False,
         default_args={"email_on_failure": True,"email": ["{{ var.value.email_recipient }}"]}) as dag:

    t1 = PythonOperator(task_id="task_1", python_callable=task_1)
    t2 = PythonOperator(task_id="task_2", python_callable=task_2)

    success = EmailOperator(
        task_id="send_success",
        to="{{ var.value.email_recipient }}",
        subject="DAG Success",
        html_content="<p>All tasks completed successfully.</p>",
        trigger_rule="all_success"
    )

    t1 >> t2 >> success
