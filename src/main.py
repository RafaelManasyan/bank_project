from src.convert_to_Py import from_xlsx_to_py, from_csv_to_py
from utils import get_info
from src.processing import filter_by_state, sort_by_date
from generators import filter_by_currency
from finding import filter_trans_by_user_input
import datetime


PATH_TO_JSON = "/Users/rafaelmanasyan/PycharmProjects/bank_project/data/operations.json"
PATH_TO_CSV = "/Users/rafaelmanasyan/PycharmProjects/bank_project/data/transactions.csv"
PATH_TO_XLSX = "/Users/rafaelmanasyan/PycharmProjects/bank_project/data/transactions_excel.xlsx"


def main():
    """General function of project"""
    transactions = []
    while True:
        menu_item = input(
            """
Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
        )
        if menu_item == "1":
            transactions = get_info(PATH_TO_JSON)
            print("Для обработки выбран JSON-файл.")
            break
        elif menu_item == "2":
            transactions = from_csv_to_py(PATH_TO_CSV)
            print("Для обработки выбран CSV-файл.")
            break
        elif menu_item == "3":
            transactions = from_xlsx_to_py(PATH_TO_XLSX)
            print("Для обработки выбран XLSX-файл.")
            break
        else:
            print("Такого пункта нет, попробуйте еще раз")
            continue
    print(transactions)
    while True:
        state_list = ["EXECUTED", "CANCELED", "PENDING"]
        trans_state = input(
            """Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
"""
        ).upper()
        if trans_state in state_list:
            state_filtered_trans = filter_by_state(transactions, state=trans_state)
            break
        else:
            print(f"Статус операции {trans_state} недоступен.")
    print(state_filtered_trans)
    while True:
        date_filtered_trans = []
        date_filter = input("Отсортировать операции по дате? Да/Нет ").title()
        if date_filter == "Да":
            vector_filter = input("Отсортировать по возрастанию или по убыванию? ").lower()
            if vector_filter == "по возрастанию":
                date_filtered_trans = sort_by_date(state_filtered_trans, vector=True)
                break
            elif vector_filter == "по убыванию":
                date_filtered_trans = sort_by_date(state_filtered_trans, vector=False)
                break
        elif date_filter == "Нет":
            date_filtered_trans = state_filtered_trans
            break
        else:
            continue
    print(date_filtered_trans)
    while True:
        rub_filter = input("Выводить только рублевые тразакции? Да/Нет ").title()
        if rub_filter == "Да":
            curr_filtered_trans = filter_by_currency(date_filtered_trans, code="RUB")
            break
        elif rub_filter == "Нет":
            curr_filtered_trans = filter_by_currency(date_filtered_trans, code="")
            break
        else:
            curr_filtered_trans = date_filtered_trans
            break
    print(curr_filtered_trans)
    while True:
        word_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").title()
        word_filtered_trans = []
        if word_filter == "Да":
            find_word = input("Введите описание транзакции: ")
            word_filtered_trans = filter_trans_by_user_input(curr_filtered_trans, find_word)
            break
        elif word_filter == "Нет":
            word_filtered_trans = curr_filtered_trans
            break
        else:
            continue

    print("Распечатываю итоговый список транзакций...")

    for trans in word_filtered_trans:
        trans_date_obj = datetime.datetime.strptime(trans["date"][:10], "%Y-%m-%d")
        new_trans_date_obj = datetime.datetime.strftime(trans_date_obj, "%d.%m.%Y")
        from_trans = f"{trans.get('from')} ->"
        if menu_item == 1:
            print(
                f"""
{new_trans_date_obj} {trans.get('description')}
{from_trans} {trans.get('to')}
Сумма: {trans.get('amount')} {trans.get("operationAmount").get("currency").get("code")}"""
            )
        elif menu_item != 1:
            print(
                f"""
{new_trans_date_obj} {trans.get('description')}
{from_trans} {trans.get('to')}
Сумма: {trans.get("operationAmount").get("amount")} {trans.get("operationAmount").get("currency").get("name")}"""
            )
