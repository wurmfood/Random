#!/usr/bin/env python3

############################
# Pascal's triangle. This isn't mine, but I came across it
# and want to hold onto it. Having it here will also hopefully
# remind me to investigate the zip idea later.
# Taken from: http://stackoverflow.com/questions/24093387/pascals-triangle-for-python
############################


def pascals_triangle(n_rows):
    results = []  # a container to collect the rows
    for _ in range(n_rows):
        row = [1]  # a starter 1 in the row
        if results:  # then we're in the second row or beyond
            last_row = results[-1]  # reference the previous row
            # this is the complicated part, it relies on the fact that zip
            # stops at the shortest iterable, so for the second row, we have
            # nothing in this list comprension, but the third row sums 1 and 1
            # and the fourth row sums in pairs. It's a sliding window.
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # finally append the final 1 to the outside
            row.append(1)
        results.append(row)  # add the row to the results.
    return results

for i in pascals_triangle(10):
    print(i)
