#!/usr/bin/env python

# Median problem
# Given a list of numbers, not in a particular order, find the median, i.e. the number that would
# locate at the middle of the sorted list.
# An O(n*log(n))-time solution is, well, just to follow the definition and sort the list.
# It turns out there is an average case O(log(n))-time solution, which is to use (part of) quicksort.
# The idea is that quicksort fixes the location of the pivot in each pass.  This gives us a good
# sense of which partition to find the eventual median.

import sys
import math

def median(xs, median_index):
    assert len(xs) > 0
    assert 0 <= median_index < len(xs)

    pivot = xs[0]
    lower_part = [x for x in xs[1:] if x <= pivot] + [pivot]
    higher_part = [x for x in xs[1:] if x > pivot]

    if median_index == len(lower_part):
        # median is the pivot
        res = pivot
    elif median_index < len(lower_part):
        res = median(lower_part, median_index)
    else:
        # median_index > len(lower_part)
        res = median(higher_part, median_index - len(lower_part))

    return res

def main(argv):
    xs = argv[1:]
    res = median(xs, math.floor(len(xs) / 2))
    print(res)

if __name__ == '__main__':
    main(sys.argv)
