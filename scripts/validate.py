from utils import log_step


def validate(datasets):

    log_step("Validating datasets")

    for name, df in datasets.items():

        print(f"\n{name}")

        print("Rows:", len(df))

        print("Duplicates:", df.duplicated().sum())

        print("Missing values")

        print(df.isna().sum())

    return datasets