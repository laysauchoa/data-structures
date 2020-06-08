import re


def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """
    size_string = len(input)
    if size_string < 2:
        return True
    if input[0] == input[len(input) - 1]:
        return palindrome(input[1:-1])
    return False


def isPalindrome(s):
    """
    Given a string, determine if it is a palindrome,
    considering only alphanumeric characters and ignoring cases.
    """
    word = re.sub('\W+', '', s).lower()

    return _isPalindrome(word)


def _isPalindrome(word):
    size_string = len(word)
    if size_string < 2:
        return True
    if word[0] == word[size_string - 1]:
        return _isPalindrome(word[1:-1])
    return False


def isPalindrome(s):
    s_in_alphanumeric = re.sub('\W+', '', s).lower()
    if list(reversed(s_in_alphanumeric)) == s_in_alphanumeric:
        return True
    return False


def isPalindrome(s):
    s_in_alphanumeric = re.sub('\W+', '', s).lower()
    if s_in_alphanumeric[::-1] == s_in_alphanumeric:
        return True
    return False

