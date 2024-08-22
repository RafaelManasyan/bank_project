import csv

import pandas as pd


def from_csv_to_py(path) -> list:
    """Function for read csv-file"""
    try:
        with open(path) as file:
            transaction_list = []
            py_file = csv.DictReader(file, delimiter=";")
            for row in py_file:
                transaction_list.append(row)
        return transaction_list
    except FileNotFoundError:
        return ["Path is not correct"]


def from_xlsx_to_py(path) -> list:
    """Function for read excel-file"""
    try:
        py_from_xlsx = pd.read_excel(path)
        py_dict = py_from_xlsx.to_dict(orient="records")
        return py_dict
    except FileNotFoundError:
        return ["Path is not correct"]
