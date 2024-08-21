from unittest.mock import patch
from src.convert_to_Py import from_csv_to_py, from_xlsx_to_py


two_trans = [
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": "3598919",
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": "29740",
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
]


@patch("src.convert_to_Py.csv.DictReader")
def test_from_csv_to_py(mock_resp):
    mock_resp.return_value = two_trans
    assert from_csv_to_py("/Users/rafaelmanasyan/PycharmProjects/bank_project/data/test_data.csv") == two_trans
    assert from_csv_to_py("") == ["Path is not correct"]


def test_from_xlsx_to_py():
    assert from_xlsx_to_py("") == ["Path is not correct"]
