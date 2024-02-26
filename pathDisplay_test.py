from program_files.pathDisplay import get_path


def test_answer():
    path = get_path([0, 2, 3, 5])
    #assert path
    print(path)
    #assert len(path) > 0
    print(len(path) > 0)
    assert type(path[0]) == str
    assert path[0].startswith("MapPieces/")
    assert path[0].endswith(".png")
    
test_answer()