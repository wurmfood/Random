#!/usr/bin/env python3


def unpacking(collection):
    """Unpacks stuff in various ways.

    >>> other_stuff = ["alice", "bob", "charlie"]
    >>> unpacking(other_stuff)
    alice bob charlie
    """
    print(*collection)


def several_args(*args):
    """
    Prints out the arguments provided.

    >>> several_args("bob")
    bob
    >>> list_of_things = ["john", "joe", "josh"]
    >>> several_args(*list_of_things)
    john
    joe
    josh
    """
    for arg in args:
        print(arg)


def quarters(next_quarter=0.0):
    """
    Takes a value and increments it by 0.25
    :param next_quarter:
    :return next_quarter + .25:

    >>> for x in quarters():
    ...   print(x)
    ...   if x >= 1.0:
    ...     break
    0.0
    0.25
    0.5
    0.75
    1.0
    """
    while True:
        yield next_quarter
        next_quarter += 0.25


def filename(initial=0):
    """
    Generates a sequential file name to be used.

    :param initial:
    :return filename:
    >>> counter = 0
    >>> for x in filename():
    ...    print(x)
    ...    counter += 1
    ...    if counter > 4: break
    0000.txt
    0001.txt
    0002.txt
    0003.txt
    0004.txt
    """
    while True:
        yield "{0:04d}.txt".format(initial)
        initial += 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()