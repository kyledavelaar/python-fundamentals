import pytest
from exercise5_count_vowels_blank import count_vowels

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("aeiouAEIOU") == 10
    assert count_vowels("") == 0