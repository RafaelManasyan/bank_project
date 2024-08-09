import json
import os

def get_info(path) -> list:
    with open(path) as file:
        py_file = json.load(file)
    return py_file


json_file_path = "operations.json"
print(get_info(json_file_path))
