#!/usr/bin/env python

# Shortest path
# Dijstra's algorithm has a nice dynmiac programming interpretation. That means sweet recursion!
# Given paths from source s to vertices v_1, ..., v_k, which are the predecessors of the destination t.
# The shortest path dist(s, t) is the minimum of the sums of dist(s, v_i) + w(v_i, t), for 1 <= i <= k.

memo = {}

class Graph(object):
    def __init__(self, edges={}, weights={}):
        self.edges = edges
        self.weights = weights

        for x in edges.keys():
            for y in edges[x]:
                if y not in self.reverse_edges:
                    self.reverse_edges[y] = [x]
                else:
                    self.reverse_edges[y] += [x]

    def dist(self, src, dst):
        if (src, dst) in memo:
            (path, min_dist) = memo[(src, dst)]
        else:
            if src == dst:
                (path, min_dist) = ([dst], 0)
            else:
                # all pairs of (pred, dist) for each predecessors of dst
                path_dists = map(lambda x: (self.dist(src, x)[0] + [dst], self.dist(src, x)[1] + self.weights[(x, dst)]), self.reverse_edges[dst])
                (path, min_dist) = min(path_dists, key=lambda x: x[1])
            memo[(src, dst)] = (path, min_dist)

        return (path, min_dist)

    def shortest_path(self, src, dst):
        return self.dist(src, dst)[0]
