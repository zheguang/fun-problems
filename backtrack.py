#!/usr/bin/env python

# Powerset problem
# Given a set of elements, generate their powerset, i.e. set of all possible subsets
# Think of it as DFS.  All solution of the same length.

import sys

class Graph(object):
    def dfs_backtrack(self, node, f_is_solution, f_successors):
        if f_is_solution(node):
            solutions = [node]
        else:
            solutions = []
            for s in list(map(lambda x: self.dfs_backtrack(x, f_is_solution, f_successors), f_successors(node))):
                solutions += s
        return solutions


def powerset(es):
    f_is_solution = lambda xs: len(xs) == len(es)

    def f_successors(xs):
        if len(xs) == len(es):
            successors = []
        else:
            successors = [xs + [es[len(xs)]], xs + ['-']]
        return successors

    graph = Graph()
    solutions = []
    for s in list(map(lambda x: graph.dfs_backtrack(x, f_is_solution, f_successors), f_successors([]))):
        solutions += s
    return solutions


def permutation(es):
    f_is_solution = lambda xs: len(xs) == len(es)

    def f_successors(xs):
        if len(xs) == len(es):
            successors = []
        else:
            # all possible insertions
            successors = list(map(lambda i: xs[0:i] + [es[len(xs)]] + xs[i:], range(len(xs) + 1)))
            print('{} - {}'.format(xs, successors))
        return successors

    graph = Graph()
    solutions = []
    for s in list(map(lambda x: graph.dfs_backtrack(x, f_is_solution, f_successors), f_successors([]))):
        solutions += s
    return solutions


def main(argv):
    mode = argv[1]
    es = argv[2:]
    if mode == 'powerset':
        print(powerset(es))
    elif mode == 'permutation':
        print(permutation(es))
    else:
        print('usage: backtrack.py [powerset|permutation] [x...]')


if __name__ == '__main__':
    main(sys.argv)
