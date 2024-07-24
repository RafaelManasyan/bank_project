def mask_account_card(acc_card_number: str) -> str:
    """Функция скрытия номера карты или номера счета"""

    if "Счет" in acc_card_number and acc_card_number != "":
        masked_info_list = "Счет ", "**", acc_card_number[-4:]
        masked_info = "".join(masked_info_list)
        return masked_info
    if "Счет" not in acc_card_number and acc_card_number != "":
        num_index = ""
        for symb in acc_card_number:
            if symb.isdigit():
                num_index = acc_card_number.find(symb)
                break
        bank_card = acc_card_number.replace(acc_card_number[(num_index + 6): (num_index + 12)], "******")
        return bank_card
    return "Введите номер карты или счет"


def get_date(system_date: str) -> str:
    """Функция получения даты из системных данных"""
    date = f"{system_date[8:10]}.{system_date[5:7]}.{system_date[0:4]}"
    return date
