import json
from datetime import datetime
from pathlib import Path
from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator

OUTPUT = Path("/opt/airflow/dags/data/api_output.json")

with DAG("http_api_interaction",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    call_api = SimpleHttpOperator(
        task_id="call_api",
        method="GET",
        http_conn_id="http_default",
        endpoint="api/v3/coins/bitcoin",
        response_filter=lambda r: r.text,
        log_response=True,
    )

    def parse_response(ti):
        data = ti.xcom_pull(task_ids="call_api")
        parsed = json.loads(data)
        if parsed.get("error"):
            raise ValueError("API error detected")
        OUTPUT.write_text(json.dumps(parsed, indent=2))
        print("Saved API output")

    t2 = PythonOperator(task_id="parse_response", python_callable=parse_response)

    call_api >> t2
