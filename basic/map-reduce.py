# -*- coding: utf-8 -*-

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i ** 2)
print(squared)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
print(squared)


def multiply(x):
    return x * x


def add(x):
    return x + x


funcs = [multiply, add]
for i in range(5):
    value = map(lambda x: x(i), funcs)
    print list(value)


number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))


from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print product