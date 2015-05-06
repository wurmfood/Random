#!/usr/bin/env python3

import math
import sys
import getopt


def sterling_approximation(n):
    n_fact = math.log(math.factorial(n))
    st_approx = n*math.log(n) - n
    error = 100*math.fabs((n_fact - st_approx)/st_approx)
    return n_fact, st_approx, error


def main(argv):
    opts, args = getopt.getopt(argv, "n:")
    fact_max = 10
    for a in args:
        print("Max: {0}".format(a))
        fact_max = int(a)

    for i in range(1, fact_max):
        fact, approx, err = sterling_approximation(i)
        print(", ".join([str(i), str(fact), str(approx), str(err)]))

############################
# Start it all up.
############################
if __name__ == "__main__":
    main(sys.argv[1:])