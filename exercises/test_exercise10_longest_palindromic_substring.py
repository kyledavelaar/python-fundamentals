import pytest
from exercise10_longest_palindromic_substring_blank import longest_palindromic_substring

def test_longest_palindromic_substring():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("ac") in ["a", "c"]