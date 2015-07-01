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


###############################
#
# Approximation method:
# ln(n!) = n*ln(n) -n
#
###############################
def sterling_approximation(n):
    n_fact = math.log(math.factorial(n))
    st_approx = n*math.log(n) - n
    err = None
    try:
        err = math.fabs((n_fact - st_approx)/n_fact)
    except ZeroDivisionError:
        err = 0
    return n_fact, st_approx, err


#################################
#
# Approximation method:
# n! = n^n * e^(-n) * sqrt(2 * Pi * n)
#
#################################
def sterling_approximation2(n):
    n_fact, st_approx, err = 0, 0, 0
    try:
        n_fact = math.factorial(n)
        st_approx = math.pow(n, n)*math.exp(-n)*math.sqrt(2*math.pi*n)
        err = math.fabs((n_fact - st_approx)/n_fact)
    except OverflowError:
        n_fact, st_approx, err = 0, 0, 0
    return n_fact, st_approx, err


def main(argv):
    opts, args = getopt.getopt(argv, "n:")
    max_num = 10

    for a in args:
        max_num = int(a)

    try:
        headers = ['n', 'ln(n!)', 'Approx', 'Err%', 'n!', 'Approx', 'Err%']
        print('{0:^4} : {1:^10} \t {2:^10} \t {3:^10} \t {4:^10} \t {5:^10} \t {6:^10}'.format(*headers))
        for i in range(1, max_num+1):
            results = []
            results[0:2] = sterling_approximation(i)
            results[3:5] = sterling_approximation2(i)
            print('{0: <4} : {1: >10.5f} '
                  '\t {2: >10.5f} \t {3: >8.3%} '
                  '\t {4: >10.5e} \t {5: >10.5e} '
                  '\t {6: >8.3%}'.format(i, *results))
    except OverflowError:
        pass
    finally:
        pass


if __name__ == "__main__":
    main(sys.argv[1:])