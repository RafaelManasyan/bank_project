import json


def get_info(path) -> list:

    try:
        with open(path) as file:
            py_file = json.load(file)
            return py_file
    except (FileNotFoundError, json.JSONDecodeError):
        return ["Ошибка"]
