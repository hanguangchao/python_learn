#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
列表生成式
'''


import os

for d in os.listdir('.'):
    print d


d = {'x': 'A', 'y': 'B', 'z': 'C' }

for x, y in d.iteritems():
    print x, y



L = ['Hello', 'World', 18, 'Apple', None]

S = [s.lower() for s in L if isinstance(s, str) == True]
print S




'''
生成器
'''


g = (x * x for x in range(0, 10))
for x in g:
    print x


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

fib(10)

print '=' * 10

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

print fib(10)

for x in fib(10):
    print x


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

print odd()

for x in odd():
    print x
    pass






def f(x):
    return x * x



print map(f, range(0, 10))


def L(x):
    return x[0:1].upper() + x[1:].lower()


print L('fdlsa')

print map(L, ['adam', 'LISA', 'barT'])


print type(123) == int

print type('123')
print type(abs)
print type(abs) == 'builtin_function_or_method'


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not (isinstance(value, int)):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100')
        self._score = value
        pass

    def __str__(self):
        return 'Student object (score: %s)' % self.score
    __repr__ = __str__


s = Student()
s.score = 60

print s.score

print s


class Fib(object):
    """docstring for Fib"""
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        if isinstance(n, int):
            for x in xrange(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
    print n


print Fib()[10]

print range(100)[5:10]


print Fib()[0:5]





class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path



print Chain().status.user.timeline.list



print callable(Student())
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('string')

print type(Student)
print type(Student())
print dir(Student)



print '=' * 100


try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print '...'


try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'


def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise


bar(0)
