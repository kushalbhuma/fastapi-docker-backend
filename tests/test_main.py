from main import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
import pytest
from fastapi import HTTPException


def test_add():
    assert add_numbers(2, 3)["result"] == 5


def test_subtract():
    assert subtract_numbers(5, 3)["result"] == 2


def test_multiply():
    assert multiply_numbers(4, 5)["result"] == 20


def test_divide():
    assert divide_numbers(10, 2)["result"] == 5


def test_divide_by_zero():
    with pytest.raises(HTTPException):
        divide_numbers(10, 0)
