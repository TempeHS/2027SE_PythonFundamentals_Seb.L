import pytest
from fuel import handling


def test_normal_Case():
    assert handling("1/2") == 50
    assert handling("3/4") == 75


def test_boundary():
    assert handling("0/5") == 0
    assert handling("5/5") == 100
    assert handling("1/3") == 33


def test_invalid_Input():
    with pytest.raises(ZeroDivisionError):
        handling("1/0")

    with pytest.raises(ValueError):
        handling("cat")
