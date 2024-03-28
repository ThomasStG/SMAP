from pathing import Graph, get_user_location
import numpy as np


def test_answer():
    g = Graph(3, )
    assert g

    d = g.dijkstra(0, 2)
    assert type(d) == list
    d = g.dijkstra(2, 1)
    assert d == [2, 0, 1]

    l = get_user_location()
    assert type(l) == tuple
