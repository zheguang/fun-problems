#!/usr/bin/env python

import sys

# linear partition problem
# input: an arrangement of positive numbers and the highest number of partitions k
# output: partition of the arrangement into subsets such that the maximum subset sum is minimized.
# example: given pages of books to scan: 100, 200, 300, 400, 500. The optimal partition is 100, 200, 300 | 400, 500

memo = dict()

def best_linear_partition(k, xs):
    if (k, len(xs)) in memo:
        (min_cost, i) = memo[(k, len(xs))]
    else:
        if k == 1 or len(xs) == 1:
            (min_cost, i) = (sum(xs), len(xs))
        else:
            def next_partition_at(i):
                (cost_left, _) = best_linear_partition(k - 1, xs[0:i])
                cost_right = sum(xs[i:])
                return (max(cost_left, cost_right), i)

            (min_cost, i) = min(map(lambda i: next_partition_at(i), range(1, len(xs) + 1)), key=lambda cost_i: cost_i[0])

        memo[(k, len(xs))] = (min_cost, i)
    return (min_cost, i)

def backtrace(k, xs):
    (_, i) = memo[(k, len(xs))]
    if k == 1 or len(xs) == 1:
        return [xs]
    else:
        return backtrace(k - 1, xs[0:i]) + [xs[i:]]

def main(argv):
    k = int(argv[1])
    xs = list(map(int, argv[2:]))

    best_linear_partition(k, xs)
    parts = backtrace(k, xs)

    print(parts)


if __name__ == '__main__':
    main(sys.argv)
