def filter_by_currency(transaction_list: list, code="USD"):
    if transaction_list is not []:
        for transaction in transaction_list:
            if transaction["operationAmount"]["currency"]["code"] == code:
                yield transaction
    else:
        return "Try again"


def transaction_descriptions(transaction_list: list):
    if transaction_list is not []:
        for transaction in transaction_list:
            yield transaction["description"]
    else:
        return "Try again"


def card_number_generator():
    for num in range(1, 9999999999999999):
        empty_num = 16 - len(f"{num}")
        joint_card = ("0" * empty_num) + f"{num}"
        card_num = " ".join([joint_card[0:4], joint_card[4:8], joint_card[8:12], joint_card[12:16]])
        yield card_num
