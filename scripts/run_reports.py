from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SQL_DIR = PROJECT_ROOT / "reports"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)

queries = [
    "total_revenue",
    "monthly_revenue",
    "top_products",
    "best_customers",
    "average_order_value",
    "daily_sales",
    "sales_by_country",
    "revenue_by_category",
]


def run_reports():

    print("=" * 60)
    print("Running SQL Reports")
    print("=" * 60)

    for report in queries:

        sql = (SQL_DIR / f"{report}.sql").read_text()

        df = pd.read_sql(sql, engine)

        output = OUTPUT_DIR / f"{report}.csv"

        df.to_csv(output, index=False)

        print(f"{report} saved to {output}")


if __name__ == "__main__":
    run_reports()