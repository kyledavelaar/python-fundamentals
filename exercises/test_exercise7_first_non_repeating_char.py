import pytest
from exercise7_first_non_repeating_char_blank import first_non_repeating_char

def test_first_non_repeating_char():
    assert first_non_repeating_char("swiss") == "w"
    assert first_non_repeating_char("aabbcc") == ""
    assert first_non_repeating_char("a") == "a"
    assert first_non_repeating_char("") == ""