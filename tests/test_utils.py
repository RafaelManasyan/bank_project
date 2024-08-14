import pytest

from src.utils import get_info


def test_get_info_file_not_found():
    assert get_info("") == ["Ошибка"]
