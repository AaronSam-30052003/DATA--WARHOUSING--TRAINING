from pathlib import Path
from datetime import datetime, timedelta
from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator

SRC = Path("/opt/airflow/dags/data/incoming/report.csv")
ARCHIVE = Path("/opt/airflow/dags/archive/")

def process_report():
    print(f"Processing {SRC}")

def archive_report():
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    SRC.rename(ARCHIVE / SRC.name)
    print(f"Archived to {ARCHIVE}")

with DAG(
    dag_id="file_sensor_pipeline",
    start_date=datetime(2025,1,1),
    schedule_interval=None,
    catchup=False
) as dag:
    wait = FileSensor(
        task_id="wait_for_report",
        filepath=str(SRC),
        poke_interval=30,
        timeout=600,
        mode="poke"
    )
    t1 = PythonOperator(task_id="process_report", python_callable=process_report)
    t2 = PythonOperator(task_id="archive_report", python_callable=archive_report)

    wait >> t1 >> t2
