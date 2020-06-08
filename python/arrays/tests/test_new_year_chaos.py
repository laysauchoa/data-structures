
import pytest
import sys

sys.path.append("..")
from new_year_chaos import minimumBribes

@pytest.mark.parametrize("test_input,expected", [([5, 1, 2, 3, 7, 8, 6, 4], "Too chaotic")])
def test_minimumBribes_too_chaotic(test_input, expected):
    assert minimumBribes(test_input) == expected

# one person can bribe only two at same time
@pytest.mark.parametrize("test_input,expected", [
    ([2, 1, 5, 3, 4], 3),

    ([1, 2, 5, 3, 4, 7, 8, 6], 4),
    ([1, 2, 5, 3, 7, 8, 6, 4], 7)])
def test_minimumBribes(test_input, expected):
    assert minimumBribes(test_input) == expected

