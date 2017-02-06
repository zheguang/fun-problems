#!/usr/bin/env python

# Edit distance
# The difference between two strings can be measured by how may "edits" one needs to transform one into the other.
# Such edits are basically shifting and copy-and-pasting.  More precisely, we can add, delete characters in one string, or substitute for characters from the other string.
# E.g.
# ...hello -> hello == ello  (shift left, or delete h)
# ...ello      ello    ello
#
# ...ello  ->  ello == hello (shift right, or add h)
# ...hello    hello    hello
#
# ...xello -> hello (substitute x for h)
# ...hello    hello
#
# Focus on the h column to think about the recursive case.  Before h column, have found the edit distance. What is the h column to do with the prefix's edit distance?

import sys

memo = {}

def edit_distance(xs, ys):
    if (xs, ys) in memo:
        res = memo[(xs, ys)]
    else:
        # base case
        if xs == '':
            res = len(ys)
        elif ys == '':
            res = len(xs)
        else:
            # recursive case, w.r.t. xs
            delete = edit_distance(xs[:-1], ys) + 1
            add = edit_distance(xs, ys[:-1]) + 1
            subs_or_keep = edit_distance(xs[:-1], ys[:-1]) + (0 if xs[-1] == ys[-1] else 1) # this parenthesis is important!

            res = min(delete, add, subs_or_keep)

        memo[(xs, ys)] = res
    return res


def main(argv):
    xs = argv[1]
    ys = argv[2]

    print(edit_distance(xs, ys))


if __name__ == '__main__':
    main(sys.argv)

