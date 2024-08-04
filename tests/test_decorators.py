import tempfile

import pytest

from src.decorators import log


def test_log_decorator(capsys):
    @log(filename="")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test2_log_decorator(capsys):
    @log(filename="")
    def my_function(x, y):
        return x + y

    my_function(1, y="m")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (1,) {'y': 'm'}\n"


def test3_log_decorator(capsys):
    @log(filename="")
    def my_function(x, y):
        return x + y

    my_function(1, "m")
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError. Inputs: (1, 'm') {}\n"


def test_log_exception_file_log(capsys):
    """Тестирует запись в файл после ошибки"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

        @log(filename=log_file_path)
        def func(x, y):
            return x + y

        func(1, "2")
        with open(log_file_path, "r", encoding="utf-8") as file:
            logs = file.read()
        assert "func error: TypeError. Inputs: (1, '2'), {}" in logs
