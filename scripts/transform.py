from utils import log_step


def transform(datasets):

    log_step("Transforming datasets")

    customers = datasets["customers"]

    customers["full_name"] = (
        customers["first_name"]
        + " "
        + customers["last_name"]
    )

    datasets["customers"] = customers

    return datasets