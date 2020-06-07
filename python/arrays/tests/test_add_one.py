import pytest
import sys

sys.path.append("..")
from add_one import add_one


def test_add_one_no_carry():
    array = [1, 2, 4]
    assert add_one(array) == [1, 2, 5]

def test_one_single():
    array = [9]
    assert add_one(array) == [1, 0]


def test_one_full_carry():
    array = [1, 9, 9]
    assert add_one(array) == [2, 0, 0]


def test_one_half_carry():
    array = [1, 8, 9]
    assert add_one(array) == [1, 9, 0]


def test_extra_value():
    array = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
    assert add_one(array) == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
