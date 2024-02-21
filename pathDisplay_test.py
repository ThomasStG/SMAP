from pathDisplay import get_path


def test_answer():
    path = get_path([1, 2, 3, 4, 5])
    assert path
    assert len(path) > 0
    assert type(path[0]) == str
    assert path[0].startswith("tempMapStuff/")
    assert path[0].endswith(".png")
