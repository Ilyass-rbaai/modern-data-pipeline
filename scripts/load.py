from sqlalchemy import create_engine

from config import DATABASE_URL
from utils import log_step


def load(datasets):

    log_step("Loading into PostgreSQL")

    engine = create_engine(DATABASE_URL)

    for table, df in datasets.items():

        df.to_sql(
            table,
            engine,
            if_exists="append",
            index=False,
        )

        print(f"{table} loaded.")