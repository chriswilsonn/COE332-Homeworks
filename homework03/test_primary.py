from primary import valid_numerical_data
from primary import top_three_years
import pytest


def test_valid_numerical_data():
    assert valid_numerical_data([{'numbers': 0},{'numbers': ''}, {'numbers': 'NaN'}, {'numbers': 55}], 'numbers') == {"Valid Rows": 2, "Invalid Rows": 2}
    assert valid_numerical_data([{'numbers': 0},{'numbers': 'NaN'}, {'numbers': 'NaN'}, {'numbers': 'var'}], 'numbers') == {"Valid Rows": 1, "Invalid Rows": 3}
    assert valid_numerical_data([{'numbers': 0},{'numbers': 'NaN'}, {'numbers': 58.22 }, {'numbers': 'var'}], 'numbers') == {"Valid Rows": 2, "Invalid Rows": 2}
    assert valid_numerical_data([{'numbers': ''},{'numbers': ''}, {'numbers': ''}, {'numbers': 'var'}], 'numbers') == {"Valid Rows": 0, "Invalid Rows": 4}
    assert valid_numerical_data([{'numbers': 0},{'numbers': 76}, {'numbers': 55.2546}, {'numbers': 22.4}], 'numbers') == {"Valid Rows": 4, "Invalid Rows": 0}

def test_top_three_years():
    assert top_three_years([{'year': '1880-01-01T00:00:00.000'},{'year': '1880-01-01T00:00:00.000'}, {'year': '1808-01-01T00:00:00.000'},{'year': '1823-01-01T00:00:00.000' }], 'year') == (['1880', '1823', '1808'] , [2, 1, 1])
    assert top_three_years([{'year': '1880-01-01T00:00:00.000'},{'year': '1880-01-01T00:00:00.000'}, {'year': '1880-01-01T00:00:00.000'},{'year': '1880-01-01T00:00:00.000' }], 'year') == (['1880'], [4])
    assert top_three_years([{'year': '1880-01-01T00:00:00.000'},{'year': '1881-01-01T00:00:00.000'}, {'year': '1882-01-01T00:00:00.000'},{'year': '1883-01-01T00:00:00.000' }], 'year') == (['1883', '1882', '1881'] , [1, 1, 1])
