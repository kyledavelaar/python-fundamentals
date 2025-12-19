import pytest
from exercise9_find_missing_number_blank import find_missing_number

def test_find_missing_number():
    assert find_missing_number([1, 2, 4, 5]) == 3
    assert find_missing_number([2, 3, 4, 5, 6]) == 1
    assert find_missing_number([1, 3]) == 2