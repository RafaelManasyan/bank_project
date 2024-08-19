import re

#
# text = 'raf klnds sdnls nsal'
# pattern = 'raf'
# strs = re.match(pattern, text)
# print(strs)


user_input_word = input('Enter word ')


def sort_trans_by_user_input(trans_list, user_input) -> list:
    pattern = user_input
    filtered_trans_list = []
    for trans in trans_list:
        trans_description = trans['description']
        if bool(re.findall(pattern, trans_description)):
            filtered_trans_list.append(trans)
    return filtered_trans_list





print(sort_trans_by_user_input(
    [{"id": 854048120,
    "state": "EXECUTED",
    "date": "2019-03-29T10:57:20.635567",
    "operationAmount": {"amount": "30234.99", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод с карты на счет",
    "from": "Visa Classic 1203921041964079",
    "to": "Счет 34616199494072692721",
     }], user_input_word))
