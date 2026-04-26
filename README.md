# Sales Pipeline — GCP + BigQuery + dbt

## Overview
End-to-end data pipeline that ingests daily sales CSV files into BigQuery
and transforms them into business-ready reporting tables using dbt.

## Tech Stack
- Python + pandas (ingestion)
- Google BigQuery (data warehouse)
- dbt Core (transformations)

## Architecture
Raw CSV → BigQuery (raw layer) → dbt staging → dbt marts → Analytics

## Models
| Model | Layer | Description |
|-------|-------|-------------|
| stg_sales | Staging | Cleaned and typed sales data |
| sales_summary | Marts | Revenue by product (completed orders only) |

## How to run
### 1. Load raw data
python load_to_bigquery.py

### 2. Run dbt transformations
dbt run

### 3. Test data quality
dbt test

## Key decisions
- Used WRITE_TRUNCATE to ensure idempotent daily loads
- Filtered cancelled and pending orders in the marts layer
- Applied lowercasing and trimming in staging to normalize product names
