#!/usr/bin/env python

# longest increasing sequence
# Given a sequence of numbers, find the longest run.  A run is a sequence of numbers that don't have to be next to each other in the original sequence.
# For example, (2, 5, 1, 6, 3, 9), the longest run is (2, 5, 6, 9).

# Given a known longest increasing sequence of a seqeucne, consider the next number and how it extends this known longest increasing sequence.
# Greedy optimal substructure doesn't always exist, becuase some suboptimal substructure may turn out to be part of the optimal final structure.

# Formulate the question as the recursive structure.

# First construct all possible next structures from the previous optimal substructures, then find the optimal next strucutre.  This order is important.  It's cross product.
# Contrast to greedy problem: construct the next optimal structure by the previous optimal substructure plus a step.  It's linear.

import sys

memo = {}

def longest_increasing_sequence(xs):
    if tuple(xs) in memo:
        (cost, seq) = memo[tuple(xs)]
    else:
        if xs == []:
            # base case
            (cost, seq) = (0, [])
        elif len(xs) == 1:
            # base case
            (cost, seq) = (1, xs)
        else:
            # recursive case
            def next_longest_increasing_sequence(i):
                (prev_cost, prev_seq) = longest_increasing_sequence(xs[i:-1])
                return (prev_cost + 1, prev_seq + [xs[-1]]) if xs[-1] >= prev_seq[-1] else (prev_cost, prev_seq)

            (cost, seq) = max(map(lambda i: next_longest_increasing_sequence(i), range(len(xs) - 1)), key=lambda cost_seq: cost_seq[0])
        memo[tuple(xs)] = (cost, seq)

    return (cost, seq)

def main(argv):
    xs = argv[1:]
    (_, seq) = longest_increasing_sequence(xs)
    print(seq)

if __name__ == '__main__':
    main(sys.argv)

