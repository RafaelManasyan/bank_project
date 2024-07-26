def get_mask_card_number(card_num: str) -> str:
    """Получаем номер карты, выводим скрытый номер карты"""
    if card_num != "":
        num_list = [num for num in card_num]
        open_nums_list = num_list[0:6] + ["*" * (len(num_list) - 10)] + num_list[-4:]
        masked_card_num = "".join(open_nums_list)
        return masked_card_num
    else:
        return "Неправильно, введите номер карты"


def get_mask_account(acc_num: str) -> str:
    """Получаем номер аккаунта и выводим две звездочки и последние 4 цифры номера"""
    if acc_num != "" and len(acc_num) > 6:
        hidden_num_list = "**", acc_num[-4:]
        hidden_acc_num = " ".join(hidden_num_list)
        return hidden_acc_num
    else:
        return "Неправильно, введите номер счета"
