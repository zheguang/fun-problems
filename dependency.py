#!/usr/bin/env python

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

            topological_order += self.dfs_dep_(root, visited, current_explore_path=[])
            unvisited -= visited

        return topological_order

    # Current explore path is added to detect cycles.  Any nodes that are on the currently explored path AND are visited again
    # are on back edges.  That said, visited nodes may be on previously explored path and hence not on the current explored path
    # and by DFS should already be included in the topological order.
    def dfs_dep_(self, root, visited, current_explore_path=[]):
        if root in current_explore_path:
            # root is on currently explored path
            raise RuntimeError('Cycle detected')
        elif root in visited:
            # root was visited in other paths, so must be included in topological order already, not a cycle.
            return []
        else:
            # root is unvivisited
            visited.add(root)

            if self.edges[root] == []:
                return [root]
            else:
                # Python doesn't have fold...
                topological_order = []
                for xs in map(lambda x: self.dfs_dep_(x, visited, current_explore_path + [root]), self.edges[root]):
                    topological_order += xs

                topological_order.append(root)

                return topological_order


def main():
    graph = Graph()
    graph.edges['A'] = ['B', 'C']
    graph.edges['B'] = ['C']
    graph.edges['C'] = []

    print(graph.dfs_dep())

if __name__ == '__main__':
    main()
