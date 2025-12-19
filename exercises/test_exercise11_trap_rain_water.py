import pytest
from exercise11_trap_rain_water_blank import trap_rain_water

def test_trap_rain_water():
    assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap_rain_water([4, 2, 0, 3, 2, 5]) == 9
    assert trap_rain_water([1, 0, 1]) == 1
    assert trap_rain_water([0, 0, 0]) == 0