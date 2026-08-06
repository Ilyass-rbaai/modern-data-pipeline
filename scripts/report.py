from sqlalchemy import create_engine, text

from config import DATABASE_URL
from utils import log_step


def run_reports():

    log_step("Running SQL Reports")

    engine = create_engine(DATABASE_URL)

    queries = {

        "Customers":
        """
        SELECT COUNT(*) AS total_customers
        FROM customers;
        """,

        "Products":
        """
        SELECT COUNT(*) AS total_products
        FROM products;
        """,

        "Orders":
        """
        SELECT COUNT(*) AS total_orders
        FROM orders;
        """,

        "Revenue":
        """
        SELECT ROUND(SUM(amount)::numeric,2) AS revenue
        FROM payments;
        """
    }

    with engine.connect() as conn:

        for title, query in queries.items():

            result = conn.execute(text(query))

            print(f"\n{title}")

            for row in result:
                print(row)