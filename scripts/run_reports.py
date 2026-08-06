from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine

from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SQL_DIR = Path(__file__).resolve().parent.parent / "postgres" / "reports"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "reports"

OUTPUT_DIR.mkdir(exist_ok=True)

queries = [
    "total_revenue",
    "monthly_revenue",
    "top_products",
    "best_customers",
    "avg_order_value",
    "daily_sales",
    "revenue_by_country",
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

        print(f"✓ {report} saved")


if __name__ == "__main__":
    run_reports()