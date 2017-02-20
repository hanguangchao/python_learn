# -*- coding: utf-8 -*-


import math

class Structurel:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Excepted {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structurel):
    _fields = ['name', 'shares', 'price']

class Point(Structurel):
    _fields = ['x', 'y']

class Circle(Structurel):
    _fields = ['radius']
    def area(self):
        return math.pi * self.radius **2


if __name__ == '__main__':
    s = Stock('abcd', 50, 91.1)

    p = Point(2, 3)

    s2 = Stock('ef', 10)


