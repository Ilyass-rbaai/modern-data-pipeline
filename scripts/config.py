from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

CUSTOMERS_FILE = DATA_DIR / "customers.csv"
PRODUCTS_FILE = DATA_DIR / "products.csv"
ORDERS_FILE = DATA_DIR / "orders.csv"
ORDER_ITEMS_FILE = DATA_DIR / "order_items.csv"
PAYMENTS_FILE = DATA_DIR / "payments.csv"

# PostgreSQL

DB_HOST = "postgres"
DB_PORT = 5432
DB_NAME = "pipeline_db"
DB_USER = "airflow"
DB_PASSWORD = "airflow"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)