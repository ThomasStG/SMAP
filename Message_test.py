from api.Messages.SendMessage import Send, Delete, Get


def test_answer():
    Send("test content")
    m = []
    m = Get()
    assert m
    assert "test content" in [x[2] for x in m]
    Delete(m[0])
    m = Get()
    assert "test content" not in m[2]
