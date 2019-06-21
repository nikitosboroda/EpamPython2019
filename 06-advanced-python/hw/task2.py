"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""
from collections import deque


class Graph:
    def __init__(self, E):
        self.E = E

    def __iter__(self):
        self.queue = deque(list(self.E)[0])
        self.val_elem = []
        return self

    def __next__(self):
        while self.queue:
            verticle = self.queue.popleft()
            if verticle not in self.val_elem:
                self.val_elem.append(verticle)
                self.queue.extend(self.E[verticle])
                return verticle
        else:
            raise StopIteration

E = {'A': ['B', 'D'], 'B': ['C'], 'C': ['E', 'F'], 'D': ['A'], 'E': ['D'], 'F': []}
graph = Graph(E)
print([f'{a}  {b}' for a in graph for b in graph])

