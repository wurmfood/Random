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


def setup_pins():
    """
    Testing how to handle pins.

    >>> setup_pins()
    5
    None

    :return:
    """
    pins = {"power_status": 6,
            "key": 5,
            "network_status": 13,
            "reset": 19,
            "ring_indicator": 26}
    print(pins["key"])
    pins["key"] = None
    print(pins["key"])


def create_message(dest_number, message):
    command = ["AT+CMGS=\"",
               dest_number,
               "\"",
               "\n",
               message,
               "\x1A"]
    msg = "".join(command).encode("ascii")
    print(msg)
    pass


class Bob:
    def __init__(self):
        self.__stuff = dict(a="alice",
                            b="bob",
                            c="charlie")

    def do_the_thing(self, thing: str):
        return thing.capitalize()

    def __getattr__(self, item):
        classname = self.__class__.__name__
        if item in self.__stuff:
            return self.do_the_thing(item)
        else:
            raise AttributeError("'{classname}' object has no "
                                 "attribute '{item}'".format(**locals()))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    create_message("4158284862", "testing")
    b = Bob()
    print(b.a)
    print(b.b)
    print(b.d)
