# -*- coding:utf-8 -*-

import math

import fractions

print dir(math)

print math.pi

print round(math.pi)
print round(math.pi, 4)

# help(round)

print float(1)
print int(-1.123)



def is_it_true(anything):
    if anything:
        print("yes, it's true")
    else:
        print("no, it's false")

def test_list():

    a_list = ['a']
    a_list = a_list + [1, 2 , 'aa']
    print a_list 
    a_list.append('b')
    a_list.append(True)
    a_list.append(0 is True)
    print a_list

    a_list.extend('extendc')
    a_list.extend(['e', 0])
    a_list.extend((1,2,3))
    a_list.extend({'kkk':'vvv'})
    print a_list
    
    print list({'kkk':'vvv'})

    a_list.insert(0, '0a')
    print a_list
    
    print a_list.count('a')
    print a_list.count('b')

    a_list.remove('a')
    a_list.pop()
    del a_list[1]
    a_list.pop(1)
    print a_list

def test_tuple():
    a_tuple = ("a", 'b', "c", 'd', 'e')
    print a_tuple, a_tuple[0], a_tuple[-1], a_tuple[1:3]


if __name__ == '__main__':
    is_it_true(1)
    is_it_true(-1)
    is_it_true(0) 
    is_it_true(0.1)
    is_it_true([])

    is_it_true(fractions.Fraction(1, 2))    


    test_list()
    test_tuple()

