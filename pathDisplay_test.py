#from program_files.pathDisplay import get_path
from pathDisplay import get_path


def test_answer():
    path = get_path([0, 2, 3, 5])
    #assert path
    #assert len(path) > 0
    assert isinstance(path[0][0], str)
    assert path[0].startswith("BoldedMap/")
    assert path[0].endswith(".png")
    