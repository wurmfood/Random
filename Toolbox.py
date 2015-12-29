#!/usr/bin/env python3

import os


# Clear the screen regardless of the OS.
# This will go away once we are storing data better.
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def sumdigits(num_to_sum):
    """Sum the individual digits of a number.
    :param num_to_sum:
    :return:

    >>> sumdigits(123)
    6
    >>> sumdigits(12.3)
    Traceback (most recent call last):
        File "E:\Python34\lib\doctest.py", line 1318, in __run
            compileflags, 1), test.globs)
        File "<doctest __main__.sumdigits[1]>", line 1, in <module>
            sumdigits(12.3)
        File ".\Toolbox.py", line 23, in sumdigits
            raise TypeError("Function requires an integer.")
    TypeError: Function requires an integer.
    >>> sumdigits(-1)
    0
    >>> sumdigits(10)
    1
    >>> sumdigits(456456)
    3
    >>> sumdigits(4564561)
    4
    """
    if type(num_to_sum) != int:
        raise TypeError("Function requires an integer.")
    if num_to_sum < 1:
        return 0
    total = num_to_sum % 10
    total += sumdigits(num_to_sum//10)
    if total > 9:
        total = sumdigits(total)
    return total


def numcheck(base, target):
    print("{0} => {1}".format(target-base, sumdigits(target-base)))
    print("{0} => {1}".format(target, sumdigits(target)))
    print("{0} => {1}".format(target+base, sumdigits(target+base)))


def listsevens():
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    a = 7
    for i in range(1, 21):
        print("{0} * {1} = {2}\t{3}".format(a, i, i*a, sumdigits(i*a)))

    numcheck(7, 7*23)
    numcheck(7, 7*23-1)
