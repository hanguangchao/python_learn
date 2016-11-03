# -*- coding=utf-8 -*-

class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    # Python 3 : def __next__(self):
    def next(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        print self.a, self.b, fib
        self.a, self.b = self.b, self.a + self.b
        print self.a, self.b, fib
        return fib

if __name__ == '__main__':
    for n in Fib(1000):
        print(n)


