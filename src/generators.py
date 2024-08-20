def filter_by_currency(transaction_list: list, code='RUB'):
    """Фильтрация транзакций по валюте"""
    new_list = []
    try:
        if transaction_list is not []:
            for transaction in transaction_list:
                if transaction.get("currency_code") == code:
                    new_list.append(transaction)
                elif code == '':
                    new_list.append(transaction)
            return new_list
    except KeyError:
        for transaction in transaction_list:
            if transaction["operationAmount"]["currency"]["code"] == code:
                new_list.append(transaction)


def transaction_descriptions(transaction_list: list):
    """Получение описания по транзакции"""
    if transaction_list is not []:
        for transaction in transaction_list:
            yield transaction["description"]
    else:
        return "Try again"


def card_number_generator():
    """Генерация номеров для банковских карт"""
    for num in range(1, 9999999999999999):
        empty_num = 16 - len(f"{num}")
        joint_card = ("0" * empty_num) + f"{num}"
        card_num = " ".join([joint_card[0:4], joint_card[4:8], joint_card[8:12], joint_card[12:16]])
        yield card_num
