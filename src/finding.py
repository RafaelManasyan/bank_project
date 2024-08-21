import re
from collections import Counter


def filter_trans_by_user_input(trans_list, user_input) -> list:
    """Function for filter transaction by user key-word"""
    pattern = user_input
    filtered_trans_list = []
    for trans in trans_list:
        trans_description = trans.get("description")
        if bool(re.findall(pattern, trans_description)):
            filtered_trans_list.append(trans)
    return filtered_trans_list


def category_counting(trans_list, category_list) -> dict:
    """Function for counting transactions by categories which in category_list"""
    all_trans_category_list = [trans["description"] for trans in trans_list if trans["description"] in category_list]
    counted = Counter(all_trans_category_list)
    return counted
