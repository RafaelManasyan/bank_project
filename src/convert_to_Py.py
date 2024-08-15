import csv
import pandas as pd


def from_csv_to_py(path):
    with open(path) as file:
        transaction_list =[]
        py_file = csv.DictReader(file, delimiter=";")
        for row in py_file:
            transaction_list.append(row)
    return transaction_list


def from_xlsx_to_py(path):
    py_from_xlsx = pd.read_excel(path)
    py_dict = py_from_xlsx.to_dict(orient='records')
    return py_dict


print(from_xlsx_to_py('/Users/rafaelmanasyan/PycharmProjects/bank_project/data/transactions_excel.xlsx'))
