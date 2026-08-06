# 🚀 Modern Data Pipeline with Apache Airflow

A complete end-to-end Data Engineering project built using modern tools and industry best practices.

This project simulates a real-world e-commerce company where raw data is extracted, validated, transformed, loaded into PostgreSQL, and automatically analyzed using Apache Airflow.

---

# 📌 Project Architecture

```
                Python Generator
                        │
                        ▼
               CSV Datasets
                        │
                        ▼
                  Airflow DAG
        ┌───────────────┴───────────────┐
        │                               │
   Extract                        Validate
        │                               │
        └───────────────┬───────────────┘
                        ▼
                   Transform
                        │
                        ▼
                     Load
                        │
                        ▼
                 PostgreSQL Database
                        │
                        ▼
                  SQL Analytics
                        │
                        ▼
                 CSV Report Outputs
```

---

# 🚀 Technologies

- Apache Airflow 3
- PostgreSQL 16
- pgAdmin 4
- Docker
- Docker Compose
- Python 3
- Pandas
- SQLAlchemy
- Faker
- NumPy

---

# 📂 Project Structure

```
modern-data-pipeline/

│
├── airflow/
│   ├── dags/
│   │      etl_pipeline.py
│   │      sql_reports.py
│   │
│   ├── logs/
│   └── plugins/
│
├── data/
│      customers.csv
│      products.csv
│      orders.csv
│      order_items.csv
│      payments.csv
│
├── postgres/
│      01_schema.sql
│      02_tables.sql
│      03_constraints.sql
│      04_seed.sql
│      05_views.sql
│
├── reports/
│      total_revenue.csv
│      monthly_revenue.csv
│      top_products.csv
│      best_customers.csv
│
├── scripts/
│      config.py
│      extract.py
│      validate.py
│      transform.py
│      load.py
│      sql_reports.py
│      utils.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# ⚙️ Features

✅ Dockerized environment

✅ PostgreSQL database

✅ pgAdmin interface

✅ Apache Airflow orchestration

✅ Automated ETL pipeline

✅ Data validation

✅ Data transformation

✅ Automatic loading into PostgreSQL

✅ Automated SQL reports

✅ CSV report generation

---

# 🗄 Database

The project contains five tables.

- Customers
- Products
- Orders
- Order Items
- Payments

Indexes and constraints are added for production-like performance.

---

# 📊 Analytics

The pipeline automatically generates:

- Total Revenue
- Monthly Revenue
- Daily Sales
- Top 10 Products
- Revenue by Category
- Best Customers
- Sales by Country
- Average Order Value

---

# 🔄 ETL Workflow

```
Extract
      │
      ▼
Validate
      │
      ▼
Transform
      │
      ▼
Load
      │
      ▼
Run SQL Reports
      │
      ▼
Save Results
```

---

# 🐳 Running the Project

## Clone repository

```bash
git clone https://github.com/your_username/modern-data-pipeline.git

cd modern-data-pipeline
```

---

## Start Docker

```bash
docker compose up -d --build
```

---

## Open Airflow

http://localhost:8080

---

## Open pgAdmin

http://localhost:5050

---

# ▶ Run the ETL

Inside Airflow

Trigger

```
etl_pipeline
```

Then

```
sql_reports
```

or schedule both DAGs.

---

# 📈 Example Outputs

The reports folder contains automatically generated CSV files.

```
reports/

total_revenue.csv

monthly_revenue.csv

top_products.csv

best_customers.csv

...
```

---

# 📚 Skills Demonstrated

- Data Engineering
- Apache Airflow
- Docker
- PostgreSQL
- SQL
- ETL Pipelines
- Data Validation
- Data Transformation
- Data Loading
- Data Analytics
- Python
- Pandas
- SQLAlchemy

---

# 🚀 Future Improvements

- PySpark instead of Pandas
- Delta Lake
- Apache Spark
- Parquet format
- Incremental Loading
- Slowly Changing Dimensions
- Data Quality Tests
- Great Expectations
- CI/CD
- Kubernetes Deployment
- AWS S3
- AWS Glue
- Databricks
## 👨‍💻 Author

Developed by **Ilyass R'BAAI**

AI & Data Science Engineering Student