import pandas as pd
from pathlib import Path
from airflow import DAG
from airflow.decorators import task
from datetime import datetime

INPUT_DIR = Path("/opt/airflow/data/input")
OUTPUT = Path("/opt/airflow/data/all_summaries.csv")

with DAG("dynamic_csv_processor",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    @task
    def list_csvs():
        return [str(p) for p in INPUT_DIR.glob("*.csv")]

    @task
    def process_file(path: str):
        df = pd.read_csv(path)
        assert list(df.columns) == ["col1", "col2", "col3"], f"Invalid headers in {path}"
        return {"file": path, "count": len(df)}

    @task
    def merge_summaries(results: list):
        df = pd.DataFrame(results)
        df.to_csv(OUTPUT, index=False)

    file_list = list_csvs()
    processed = process_file.expand(path=file_list)
    merge_summaries(processed)
