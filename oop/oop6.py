# -*- coding: utf-8 -*-

class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, cls):
        print('__get__<<')
        print(instance)
        print(cls)
        print('__get__>>')
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self, instance, value):
        print(self)
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected ' + str(self.expected_type))
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]
    def __str__(self):
        return "Typed name: %s , expected_type:%s" % (self.name, self.expected_type)

def typeassert(**kwargs):
    def decorate(cls):
        print(cls)
        for name, expected_type, in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate

@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name 
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('a', 12, 11.11)
    print(s)
    print(s.name)
