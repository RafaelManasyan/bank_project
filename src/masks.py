def get_mask_card_number(card_num: str) -> str:
    """Получаем номер карты, выводим скрытый номер карты"""
    card_num_clear = card_num.split(" ")
    hidden_num_list = (
        card_num_clear[0][0:4],
        (str(card_num_clear[0][4:6] + "**")),
        "****",
        card_num_clear[0][12:16],
    )
    hidden_num = " ".join(hidden_num_list)
    return hidden_num


def get_mask_account(acc_num: str) -> str:
    """Получаем номер аккаунта и выводим две звездочки и последние 4 цифры номера"""
    hidden_num_list = "**", acc_num[-4:]
    hidden_acc_num = " ".join(hidden_num_list)
    return hidden_acc_num
