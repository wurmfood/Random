#!/usr/bin/env python3

##########################
#
# Brief implementation of the Sterling Approximation for factorials.
#
# Takes one argument: maxnum which is the maximum value the factorial will be
# calculated for. It outputs ln(n!), the approximation, and the error percentage.
#
##########################

import math
import sys
import getopt


def sterling_approximation(n):
    n_fact = math.log(math.factorial(n))
    st_approx = n*math.log(n) - n
    err = math.fabs((n_fact - st_approx)/st_approx)
    return n_fact, st_approx, err


def main(argv):
    opts, args = getopt.getopt(argv, "n:")
    max_num = 10

    for a in args:
        max_num = int(a)

    try:
        print('{0:^4} : {1:^10} \t {2:^10} \t {3:^10}'.format('n', 'ln(n!)', 'Approx', 'Err%'))
        for i in range(1, max_num+1):
            fact, approx, error = sterling_approximation(i)
            print('{0: <4} : {1: >10.5f} \t {2: >10.5f} \t {3: >8.3%}'.format(i, fact, approx, error))
    finally:
        pass


if __name__ == "__main__":
    main(sys.argv[1:])