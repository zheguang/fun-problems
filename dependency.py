#!/usr/bin/env python

from random import random
from math import floor

class Graph:
    def __init__(self, edges={}):
        self.edges = edges

    # This does not work for sibling edges in triangle pattern, for this counterexample:
    # A: B, C
    # C: B
    # one of the possible bfs visiting orders: A B C
    def bfs_dep(self):
        start = list(self.edges.keys())[0]
        visited = []
        queue = [start]
        while len(queue) > 0:
            next = queue.pop() # remove the last item
            if next not in visited:
                visited.append(next)
            queue = self.edges[next] + queue # add new items to the front
        return visited

    def dfs_dep(self):
        topological_order = []
        visited = set()
        unvisited = set(self.edges.keys())
        while unvisited != set():
            root = list(unvisited)[0]
            topological_order += self.dfs_dep_(root, visited)
            unvisited -= visited

        return topological_order

    def dfs_dep_(self, root, visited):
        if root in visited:
            return []
        else:
            visited.add(root)

            if self.edges[root] == []:
                return [root]
            else:
                # Python doesn't have fold...
                topological_order = []
                for xs in map(lambda x: self.dfs_dep_(x, visited), self.edges[root]):
                    topological_order += xs

                topological_order.append(root)

                return topological_order


def main():
    graph = Graph()
    graph.edges['D'] = []
    graph.edges['A'] = ['B', 'C']
    graph.edges['B'] = ['C', 'D']
    graph.edges['C'] = ['D']

    print(graph.dfs_dep())

if __name__ == '__main__':
    main()
