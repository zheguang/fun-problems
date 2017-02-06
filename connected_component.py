#!/usr/bin/env python

# Connected component problem
# Given a graph, find all connected components and their interconnects.
# A connected component is a subgraph where "any node can go to any other node", or there exists a path connecting each pair of node.

# clique: anyone goes to anyone
# strongly connected: anyone goes to anyone (including oneself) through someone
# weakly connected: as long as there is an edge
# For undirected graph, strongly connected is the same as weakly connected.

class Graph(object):
    def __init__(self, edges={}):
        self.edges = edges

    def strongly_connected_components(self):
        # i.e. anyone can go to anyone
        # Find all cycles
        cycle_groups = self.dfs_lambda(self.dfs_cycles)

        # Merge intersected cycles into same connected component
        #return union_intersected_sets(cycles)
        components = []
        for x in map(lambda x: union_intersected_sets(list(map(set, x))), cycle_groups):
            components += x

        return components

    def weakly_connected_components(self):
        # i.e. disconnected subgraphs
        # first, convert one-way streets to two-way streets
        undirected_graph = Graph(dict(self.edges))
        for x in self.edges.keys():
            for y in self.edges[x]:
                if x not in undirected_graph.edges[y]:
                    undirected_graph.edges[y] += [x]

        visiteds = undirected_graph.dfs_lambda(undirected_graph.dfs_weakly_connected)
        # visiteds should be a list of monotonically increasing graph partitions, i.e. visiteds[i] is a subgraph of visiteds[j] for i < j
        # and their difference is the graph parittions.
        components = [visiteds[0]] + list(map(lambda i: visiteds[i] - visiteds[i - 1], range(1, len(visiteds))))
        return components

    def dfs_lambda(self, f_dfs):
        # Find all cycles
        visited = set()
        vals = []
        while visited != set(self.edges.keys()):
            start = list(set(self.edges.keys()) - visited)[0]
            (visited, val) = f_dfs(start, visited)
            vals += [val]
        return vals

    def dfs_cycles(self, node, visited, current_explore_path=[]):
        if node in current_explore_path:
            # cycle detected
            cycles = [current_explore_path[current_explore_path.index(node):]]
        elif node in visited:
            cycles = []
        else:
            visited = visited.union([node])
            #cycles = [y for y in map(lambda x: self.dfs_cycles(x, visited, current_explore_path + [node])[1], self.edges[node]) if y != []]
            cycles = []
            for x in self.edges[node]:
                (visited, cs) = self.dfs_cycles(x, visited, current_explore_path + [node])
                cycles += cs #if cs != [] else [x]

        return (visited, cycles)

    # one-way or two-way street graph
    def dfs_weakly_connected(self, node, visited, current_explore_path=[]):
        if node in current_explore_path:
            # cycle detected
            pass
        elif node in visited:
            pass
        else:
            visited = visited.union([node])
            for x in self.edges[node]:
                (visited, _) = self.dfs_weakly_connected(x, visited, current_explore_path + [node])

        return (visited, visited)


# TODO: abstract as graph contruction from custom edge function
def union_intersected_sets(sets):
    # model as a graph problem:
    # each set is a node, if two sets intersected, then they share an edge.
    # unions of interested sets is to find graph partitions that are disconnected
    if sets == []:
        return []
    else:
        nodes = list(range(len(sets)))
        graph = Graph(dict(map(lambda x: (x, []), nodes)))
        for (x, y) in [(x, y) for x in nodes for y in nodes if x != y]:
            if sets[x].intersection(sets[y]) != set():
                graph.edges[x] += [y]
                graph.edges[y] += [x]

    components = graph.weakly_connected_components()
    union_sets = []
    for c in components:
        union_set = set()
        for node in c:
            union_set = union_set.union(sets[node])
        union_sets += [union_set]

    return union_sets




def main():
    #edges = { 1: [2], 2: [4], 3: [1], 4: [3], 5: [3, 4, 6], 6: [7], 7: [5], 8: [10], 9: [8], 10: [9, 11], 11: [10, 13], 12: [11], 13: [] }
    edges = { 1: [2], 2: [3, 4], 3: [2], 4: [5], 5: [4] }
    graph = Graph(edges)
    print(graph.strongly_connected_components())

if __name__ == '__main__':
    main()
