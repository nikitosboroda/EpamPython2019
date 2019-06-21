"""
Написать тесты(pytest) к предыдущим 3 заданиям, запустив которые, я бы смог бы проверить их корректность
"""
# py.test -v -s task4.py
from task2 import Graph
from task3 import ShiftDescriptor, CeasarSipher
import pytest


@pytest.mark.parametrize('graph, expected', [
    ({'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A', 'R'], 'R': []}, ['A', 'B', 'C', 'D', 'R']),
    ({'A': ['B', 'C', 'D', 'R'], 'B': ['C'], 'C': [], 'D': ['A', 'E'], 'R': [], 'E': ['F'], 'F': []},
     ['A', 'B', 'C', 'D', 'R', 'E', 'F']),
    ({'A': ['B', 'D'], 'B': ['C'], 'C': ['E', 'F'], 'D': ['A'], 'E': ['D'], 'F': []}, ['A', 'B', 'D', 'C', 'E', 'F'])
])
def test_task2(graph, expected):
    """Test BFS in task2"""
    assert [vertice for vertice in Graph(graph)] == expected


@pytest.fixture()
def caesar():
    obj = CeasarSipher()
    obj.message = 'abc'
    obj.another_message = 'hello'
    obj.other = 'ZeNA'
    return obj


def test_task3(caesar):
    """Test task3 Caesar Cipher"""
    assert caesar.message == 'efg'
    assert caesar.another_message == 'olssv'
    assert caesar.other == 'OtCP'
