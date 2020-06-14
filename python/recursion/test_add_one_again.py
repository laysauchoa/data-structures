
import pytest
import sys

from ..add_one_again import add_one_again

@pytest.mark.parametrize("input, answer", [
    ([1, 2, 3], [1, 2, 4]
    )])
def test_add_one_again(input, answer):
    assert add_one_again(input) == answer
