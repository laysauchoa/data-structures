import pytest
import sys

from ..duplicate_number import duplicate_number


@pytest.mark.parametrize("array_input, repeated_number", [
    ([0, 2, 3, 1, 4, 5, 3], 3),
    ([0, 0], 0),
    ([0, 1, 5, 5, 3, 2, 4], 5)

], ids=[
    'mix array with number repeated 3',
    'arrays of composed of zero with 0 repeated',
    'mix array with number repeated 5',
])
def test_duplicate_number(array_input, repeated_number):
    assert duplicate_number(array_input) == repeated_number
