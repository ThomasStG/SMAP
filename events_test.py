from os.path import abspath, dirname
from datetime import datetime
import pytest
from program_files.events import getEvents



def test_answer():
    e = getEvents()

    assert e
    if len(e) != 0:
        assert type(e) == list
        assert type(e[0][0]) == str
        format_str = "%A, %B %d, %Y, %I:%M %p"
        datetime_str = e[0][1].replace('\xa0', ' ')
        assert datetime.strptime(datetime_str, format_str)
        assert type(e[0][1]) == str
        assert type(e[0][2]) == str
        assert type(e[0][3]) == str
    # ('Blood Drive Tabling', 'Tuesday, February\xa020, 2024, 9:00\xa0AM', 'Student Center- Hallway Table Space 1, Academic Center - Table 1.', 'No Description')
