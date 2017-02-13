#!/usr/bin/env python

# Longest common sequence
# Given two strings, the task is to find the longest common sequence of letters among them.
# The letters do not have to be next to each other in the original string.
# E.g. C D E F G A B
#      D E G B R T Z
# output: D E G B
#
# It is interesting to compare this problem to longest increasing sequence.
# The subproblem search space is different.
# In longest increasing sequence, the search space is the LIS[i:-1] for all i.
# But for longest common sequence, the search space is similat to the edit distance
# i.e. LCS[0:-1].
# To determine the proper search space, it is important to know what the final optimal
# answer might be from.

memo = {}

def longest_common_sequence(xs, ys):
    if (tuple(xs), tuple(ys)) in memo:
        lcs = memo[(tuple(xs), tuple(ys))]
    else:
        # can't use xs == [] comparison because string xs and list xs is different in python.
        if len(xs) == 0 or len(ys) == 0:
            lcs = []
        else:
            lcs = max([
                longest_common_sequence(xs[:-1], ys),
                longest_common_sequence(xs, ys[:-1]),
                longest_common_sequence(xs[:-1], ys[:-1]) + [xs[-1]] if xs[-1] == ys[-1] else []
                ],
                key=lambda xs: len(xs))
        memo[(tuple(xs), tuple(ys))] = lcs
    return lcs

def main():
    xs = 'helloworld'
    ys = 'foobarbusdust'
    lcs = longest_common_sequence(xs, ys)
    print(lcs)

if __name__ == '__main__':
    main()
