import pytest
from exercise4_max_product_blank import max_product

def test_max_product():
    assert max_product([1, 2, 3, 4]) == 12
    assert max_product([-10, -20, 5, 6]) == 200
    assert max_product([-10, 10, 5, 6]) == 60
    assert max_product([0, 0, 0]) == 0
    assert max_product([1]) == 0