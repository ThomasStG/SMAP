"""from api.Messages.SendMessage import Send, Delete, Get


def test_answer():
    Send("x4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5")  # test send
    m = Get()  # test get
    assert m
    for x in m:  # remove the row added
        if "x4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5" in x[2]:
            Delete(x[0])
    m = Get()
    assert "x4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5" not in [
        x[2] for x in m]  # test the delete call. Ensure message deleted is gone.
    Send("x4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5e x4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5ex4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5e")  # attempt to insert message over 250 characters
    m = Get()
    assert "x4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5e x4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5ex4Fu1Gfw9sXwJN28vQXZ4l0Nfqj1vZd07S9Zc4MdZa8zm8vJDNn4d2PQ12Qjvc52XzJ9wG6lI4l6QKSc0CX3wR57Zx3A0i0h9P5e" not in [
        x[2] for x in m]  # ensure not added"""