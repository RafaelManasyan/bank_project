import pytest

from src.decorators import log


def test_log_decorator(capsys):
    @log(filename='')
    def my_function(x, y):
        return x + y
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\n'
