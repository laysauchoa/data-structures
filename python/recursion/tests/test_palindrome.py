
import pytest
import sys

from ..palidrome import is_palindrome, isPalindrome

@pytest.mark.parametrize("word, is_palindrome", [
    ("abba", True),
    ("casa", False),
    ("rotor", True),
    ("", True)

], ids=[
    'valid even palindrome word',
    'not a palindrome word',
    'valid odd palindrome word',
    'empty string is palindrome'
])
def test_palindrome(word, is_palindrome):
    assert is_palindrome(word) == is_palindrome


@pytest.mark.parametrize("sentence, answer", [
    ("race a car", False),
    ("A man, a plan, a canal: Panama", True),
    ("", True)

], ids=[
    'valid palindrome sentence',
    'not a palindrome sentence',
    'empty string'
])
def test_palindrome(sentence, answer):
    assert isPalindrome(sentence) is answer
