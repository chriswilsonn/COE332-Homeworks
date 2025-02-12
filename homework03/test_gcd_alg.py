from gcd_algorithm import great_circle_distance
import pytest

def test_great_circle_distance():
    assert great_circle_distance(50.66667, 2.33333, 13.66033, 28.96) == 4768.875608610178
    with pytest.raises(TypeError):
        great_circle_distance('50.66667', 2.33333, 13.66033, 28.96)
    with pytest.raises(TypeError):
        great_circle_distance('NaN', 0, 13.66033, 28.96)
    assert great_circle_distance(2,45.66,0, 33) == 1426.4680861654447 

