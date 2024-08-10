import json


def get_info(path) -> list:
    with open(path) as file:
        py_file = json.load(file)
    return py_file