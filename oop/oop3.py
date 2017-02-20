# -*- coding:utf-8 -*-

class Person:
    def __init__(self, first_name):
        self.first_name  = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        try:
            if not isinstance(value, str):
                raise TypeError('Excepted a string')
            self._first_name = value
        except TypeError as e:
            print(e)

    @first_name.deleter
    def first_name(self, value):
        raise AttributeError("Can't delete attribute")

def testPerson():
    a = Person('Guido')
    print(a.first_name)
    a.first_name  = 2
    print(a.first_name)
    a.first_name = 'ha'
    print(a.first_name)



class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        try:
            if not isinstance(value, str):
                raise TypeError('Excepted a string')
            self._first_name = value
        except TypeError as e:
            print(e)

    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    name = property(get_first_name, set_first_name, del_first_name)

def testPerson2():
    b = Person2('bbbb')
    print(b)
    print(b.name)
    print(Person2('cccc'))
    


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2 

    @property
    def diameter(self):
        return radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

def testCircle():
    c = Circle(4.0)
    print(c.radius)
    print(c.area)
    print(c.perimeter)

if __name__ == '__main__':
    testPerson()
    testPerson2()
    testCircle()
    """
    Guido
    Traceback (most recent call last):
      File "oop3.py", line 24, in <module>
        a.first_name  = 2
      File "oop3.py", line 14, in first_name
        raise TypeError('Excepted a string')
    TypeError: Excepted a string
    """

