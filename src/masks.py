import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(asctime)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_num: str) -> str:
    """Получаем номер карты, выводим скрытый номер карты"""
    logger.info("Получили номер карты")
    if card_num != "":
        num_list = [num for num in card_num]
        open_nums_list = num_list[0:6] + ["*" * (len(num_list) - 10)] + num_list[-4:]
        masked_card_num = "".join(open_nums_list)
        logger.info("Получили скрытый номер карты")
        return masked_card_num
    else:
        logger.error("Неподходящий номер карты")
        return "Неправильно, введите номер карты"


def get_mask_account(acc_num: str) -> str:
    """Получаем номер аккаунта и выводим две звездочки и последние 4 цифры номера"""
    logger.info("Получен номер аккаунта")
    if acc_num != "" and len(acc_num) > 6:
        hidden_num_list = "**", acc_num[-4:]
        hidden_acc_num = " ".join(hidden_num_list)
        logger.info("Получили скрытый номер аккаунта")
        return hidden_acc_num
    else:
        logger.error("Неподходящий номер аккаунта")
        return "Неправильно, введите номер счета"


get_mask_card_number("73654108430135854893")
get_mask_account("")
