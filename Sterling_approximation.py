#!/usr/bin/env python3

import math
import sys
import getopt


def sterling_apprixmation(n):
    n_fact = math.log(math.factorial(n))
    st_approx = n*math.log(n) - n
    err = 100*math.fabs((n_fact - st_approx)/st_approx)
    return n_fact, st_approx, err


def main(argv):
    opts, args = getopt.getopt(argv, "n:")
    max_num = 10

    for a in args:
        max_num = int(a)

    try:
        for i in range(1, max_num+1):
            fact, approx, error = sterling_apprixmation(i)
            print('{0} : {1}, {2}, {3}'.format(i, fact, approx, error))
    finally:
        pass


if __name__ == "__main__":
    main(sys.argv[1:])