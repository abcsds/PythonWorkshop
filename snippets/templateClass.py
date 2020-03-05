#!/usr/bin/env python3


# https://docs.python.org/3/reference/datamodel.html#special-method-names
class MyClass(object):
    var = 0

    def __init__(self, args, data):  # Constructor
        super().__init__()
        self.data = data
        self.index = self.var
        self.max = len(data)
        self.args = args

    def __repr__(self):  # Representation string
        return self.args

    def __str__(self):  # Printable method
        return "The index is " + str(self.index)

    def __iter__(self):  # A function for an iterable
        return self

    def __next__(self):  # A fonction for the next iterable data
        if self.index == self.max - 1:
            raise StopIteration
        self.index = self.index + 1
        return self.data[self.index]
