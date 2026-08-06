import pandas as pd

from config import (
    CUSTOMERS_FILE,
    PRODUCTS_FILE,
    ORDERS_FILE,
    ORDER_ITEMS_FILE,
    PAYMENTS_FILE,
)

from utils import log_step


def extract():

    log_step("Extracting datasets")

    datasets = {
        "customers": pd.read_csv(CUSTOMERS_FILE),
        "products": pd.read_csv(PRODUCTS_FILE),
        "orders": pd.read_csv(ORDERS_FILE),
        "order_items": pd.read_csv(ORDER_ITEMS_FILE),
        "payments": pd.read_csv(PAYMENTS_FILE),
    }

    for name, df in datasets.items():
        print(f"{name}: {df.shape}")

    return datasets


if __name__ == "__main__":
    extract()