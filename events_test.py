"""Module test case for events.py."""
from datetime import datetime
from events import getEvents


def test_answer():
    """Test function for events.py"""
    e = getEvents()

    assert e
    if len(e) != 0:
        assert isinstance(e, list)
        assert isinstance(e[0][0], str)
        format_str = "%A, %B %d, %Y, %I:%M %p"
        datetime_str = e[0][1].replace('\xa0', ' ')
        assert datetime.strptime(datetime_str, format_str)
        assert isinstance(e[0][1], str)
        assert isinstance(e[0][2], str)
        assert isinstance(e[0][3], str)
    # ('Blood Drive Tabling', 'Tuesday, February\xa020, 2024, 9:00\xa0AM',
    # 'Student Center- Hallway Table Space 1, Academic Center - Table 1.', 'No Description')
