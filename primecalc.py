#!/usr/bin/env python3
from math import sqrt, ceil
from datetime import datetime

# So, basic idea:
# Look at odd numbers only (even numbers can't be prime)
# Go from 3 to the square root of the target number.
# Check to see if the number can be divided into the target with no remainder


def check_if_prime(target: int) -> bool:
    """
    Returns True if the target is a prime number.
    :param target: int representing number to check
    :return: bool that is True if target is prime
    :rtype: bool
    """
    if target < 4:
        # 1, 2, and 3 are all prime, so don't check.
        return True
    for i in range(2, ceil(sqrt(target))+2):
        # Do the thing
        if target % i == 0:
            return False
    return True


def main(max_number: int) -> None:
    count = 0
    start_time = datetime.now()
    for num in range(1, max_number):
        if check_if_prime(num):
            count += 1
    print("Total prime numbers from 0 to {0} : {1}".format(max_number, count))
    print("Time taken: {0}".format(datetime.now() - start_time))

if __name__ == "__main__":
    maximum = 1000000
    main(maximum)
