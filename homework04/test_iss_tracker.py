import pytest
from iss_tracker import year_range
from iss_tracker import matching_time
from iss_tracker import speed

def test_year_range():
    assert year_range([{'EPOCH': '2025-045T10:38:30.000Z'},{'EPOCH': '2025-055T10:38:30.000Z'}, {'EPOCH': '2025-065T10:38:30.000Z'}, {'EPOCH': '2025-065T08:42:30.000Z'}], 'EPOCH')     ==  ('February 14, 2025', 'March 06, 2025')
    assert year_range([{'EPOCH': '2025-045T10:38:30.223Z'},{'EPOCH': '2025-055T10:38:30.150Z'}, {'EPOCH': '2025-065T10:38:30.000Z'}, {'EPOCH': '2025-065T08:42:30.000Z'}], 'EPOCH')     ==  ('February 14, 2025', 'March 06, 2025')
    assert year_range([{'EPOCH': '2025-045T10:38:30.223'},{'EPOCH': '2025-055T10:38:30.150Z'}, {'EPOCH': '2025-065T10:38:30.000'}, {'EPOCH': '2025-065T08:42:30.000Z'}], 'EPOCH') == 'Invalid Date Format'

def test_matching_time():
    assert matching_time([{'EPOCH': '2025-045T10:38:30.000Z'},{'EPOCH': '2025-055T10:38:30.000Z'}, {'EPOCH': '2025-065T10:38:30.000Z'}, {'EPOCH': '2025-051T16:47:30.000Z'}], 'EPOCH') == None

    assert matching_time([{'EPOCH': '2025-045T10:38:30.000Z'},{'EPOCH': '2025-047T10:28:18.000Z'}, {'EPOCH': '2025-065T10:55:30.000Z'}, {'EPOCH': '2025-071T16:47:30.000Z'}], 'EPOCH') == None
    
    with pytest.raises(ValueError):
        matching_time([{'EPOCH': '2025-045T10:38:30.000Z'},{'EPOCH': '2025-0475T10:28:18.000Z'}, {'EPOCH': '2025-065T10:55:30.000Z'}, {'EPOCH': '2025-071T16:47:30.000Z'}], 'EPOCH')

def test_speed():
    assert speed()
