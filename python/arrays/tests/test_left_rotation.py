import pytest
from ..left_rotation import rotate


def test_empty_list():
    d = 10
    list_1 = []

    assert rotate(d, list_1) == []

    d = 0
    list_1 = [1, 2, 3, 4]

    assert rotate(d, list_1) == [1, 2, 3, 4]


def test_rotate():
    d = 4
    lista = [1, 2, 3, 4, 5]

    assert rotate(d, lista) == [5, 4, 3, 2, 1]


def test_rotate():
    d = 2
    lista = [1, 2, 3, 4, 5]

    assert rotate(d, lista) == [3, 4, 5, 1, 2]
