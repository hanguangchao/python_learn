# -*- coding:utf-8 -*-

class Person:
    def __init__(self, name):
        self.name  = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        try:
            if not isinstance(value, str):
                raise TypeError('Excepted a string')
            self._name = value
        except TypeError as e:
            print(e)

    @name.deleter
    def name(self, value):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    """docstring for SubPerson"""
    def __init__(self, arg):
        super(SubPerson, self).__init__()
        self.arg = arg
        
    def name(self):
        print('Getting name')
        return super().name

    def name(self, value):
        print('Setting name to ', value)
        super(SubPerson, SubPerson).name.__set(self, value)

    @name.deleter
    def name(self, value):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)

print super.__doc__
