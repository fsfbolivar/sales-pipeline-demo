from google.cloud import bigquery
import pandas as pd

def load_sales_to_bigquery():
    client = bigquery.Client()
    
    df = pd.read_csv("data/sales_raw.csv")
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["load_timestamp"] = pd.Timestamp.now()
    
    table_id = "sales-pipeline-demo-777.raw.sales_raw"  # <- reemplaza aquí
    
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
    )
    
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()
    
    print(f"✅ Loaded {len(df)} rows to {table_id}")

if __name__ == "__main__":
    load_sales_to_bigquery()
