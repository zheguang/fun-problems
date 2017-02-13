#!/usr/bin/env python

# Minimum spanning tree
# A spanning tree of a graph contains all vertices and some edges from the graph and is a tree, i.e. no cycles and one root.
# A minimum spanning tree has the lowest sum of edge weights.
# Applications:
# - identify natural clusters: just remove the 'longest' edges in the MST.
# - provide approximate solution to travel salesman problem (and other hard problems).

class Graph(object):
    def __init__(self, edges={}, weights={}):
        self.edges = edges

    def prim(self, tree, nontree=[]):
        (node, min_dist) = min(nontree, key=lambda x: x[1])

        assert node not in tree.edges
        assert self.edges[node] in tree.edges
        tree.edges[self.edges[node]] += [node]
        tree.edges[node] = []

        nontree = [(x[0], min(x[1], self.weights[(x[0], node)])) for x in nontree if x != (node, min_dist)]

        if nontree != []:
            return self.prim(tree, nontree)
        else:
            return tree


class Tree(Graph):
    def __init__(self, edges={}, weights={}, root=None):
        super().__init__(edges, weights)
        self.root = root

