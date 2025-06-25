import pandas as pd
from pathlib import Path
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

SRC = Path("/opt/airflow/dags/data/orders.csv")

def validate():
    df = pd.read_csv(SRC)
    required = {"order_id", "customer_id", "amount"}
    if not required.issubset(df.columns):
        raise ValueError(f"Missing columns: {required - set(df.columns)}")
    if df[["order_id", "customer_id", "amount"]].isnull().any().any():
        raise ValueError("Null values found in mandatory fields")
    print("Validation passed")
    return True

def summarize():
    df = pd.read_csv(SRC)
    print(df.groupby("customer_id")["amount"].sum())

with DAG("data_quality_validation",
         start_date=datetime(2025,1,1),
         schedule_interval=None,
         catchup=False) as dag:

    t1 = PythonOperator(task_id="validate", python_callable=validate)
    t2 = PythonOperator(task_id="summarize", python_callable=summarize)

    t1 >> t2
