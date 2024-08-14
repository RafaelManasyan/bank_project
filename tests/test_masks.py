import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def test_right_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "700079******6361"


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("401288881888", "401288**1888"),
        ("4012888818888", "401288***8888"),
        ("37598765432100", "375987****2100"),
        ("375987654321001", "375987*****1001"),
        ("70007922896063610", "700079*******3610"),
        ("700079228960636101", "700079********6101"),
        ("7000792289606361012", "700079*********1012"),
    ],
)
def test_len_get_mask_card_number(user_input, expected):
    assert get_mask_card_number(user_input) == expected


@pytest.fixture
def test_empty_get_mask_card_number():
    assert get_mask_card_number("") == "Неправильно, введите номер карты"


@pytest.mark.parametrize(
    "user_input, expected",
    [("73654108430135874305", "** 4305"), ("73654108430135854893", "** 4893")],
)
def test_right_get_mask_account(user_input, expected):
    assert get_mask_account(user_input) == expected


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("73654108430135854893", "** 4893"),
        ("736541084301358548931231231", "** 1231"),
        ("123123213023002", "** 3002"),
        ("", "Неправильно, введите номер счета"),
        ("3221", "Неправильно, введите номер счета"),
    ],
)
def test_len_get_mask_account(user_input, expected):
    assert get_mask_account(user_input) == expected
