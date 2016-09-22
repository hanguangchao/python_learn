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


if __name__ == '__main__':
    is_it_true(1)
    is_it_true(-1)
    is_it_true(0) 
    is_it_true(0.1)
    is_it_true([])

    is_it_true(fractions.Fraction(1, 2))    
