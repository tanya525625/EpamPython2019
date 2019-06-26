"""
E - dict(<V> : [<V>, <V>, ...])
Ключ - строка, идентифицирующая вершину графа
значение - список вершин, достижимых из данной

Сделать так, чтобы по графу можно было итерироваться(обходом в ширину)

"""
from queue import Queue


class GraphIterator:

    def __init__(self, graph):
        self.E = E
        self.nodes_count = len(self.E.keys())
        self.processed = [tuple(self.E.keys())[0]]
        self.nodes_queue = Queue()
        self.nodes_queue.put(tuple(self.E.keys())[0])

    def __next__(self):
        while not self.nodes_queue.empty():
            curr_node = self.nodes_queue.get()
            for neighbour_node in self.E[curr_node]:
                if neighbour_node not in self.processed:
                    self.nodes_queue.put(neighbour_node)
                    self.processed.append(neighbour_node)
            return curr_node        
        raise StopIteration
    
    def __iterator__(self):
        return self


class Graph:
    
    def __init__(self, E):
        self.E = E
        
    def __iter__(self):
        return GraphIterator(self)

   
        
E = {'A': ['B', 'C', 'D'], 'B': ['C'], 'C': [], 'D': ['A']}
