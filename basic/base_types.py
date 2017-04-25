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


def test_numeric():
    x = 1231.92391931123983357
    print x
    """
    制定宽度和精度
    '[<>^]?width[,]?(.digits)?' 
    """
    print format(x, '0.2f')
    print format(x, '>10.1f')
    print format(x, '<10.6f')
    print format(x, '^10.1f')
    print format(x, ',')
    print format(x, '0,.2f')

    print format(x, 'e')
    print format(x, '0.2E')

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
    print 'a' in a_tuple
    print 'e' in a_tuple
    print a_tuple.index('a')
    print a_tuple.index('e')

    v = ('a', 2, True)
    (x, y, z) = v
    print x, y , z 

def test_set():
    a_set = {1, 2, 3}
    print a_set
    print type(a_set)
    a_set = {1, 2}
    print a_set

    a_list = [1, 2, 3, 'sss', 'ooo']
    a_set = set(a_list)
    print a_set
    print a_list
    print len(a_set)
    print len(a_list)
    a_set.add('eee')
    print a_set
    a_set.update([5, 6 , 7 , False, 'ok'])
    print a_set
    
    other_set = a_set

    a_set.discard('eee')
    a_set.remove('sss')
    print a_set
    a_set.pop()
    print a_set
    print other_set
    a_set.clear()
    print a_set
    print other_set

    a_set = {1, 2, 'a', 'b', 'e', 'f'}
    b_set = {'a', 'b', 'c'}
    print a_set.union(b_set)
    print a_set.intersection(b_set)
    print a_set.difference(b_set)
    
    a_set = {1, 2, 3}
    b_set = {1, 2, 3, 4}
    print a_set.issubset(b_set)
    print b_set.issuperset(a_set)
    
    a_set.add(5)
    print a_set.issubset(b_set)
    print b_set.issuperset(a_set)

def test_dict():
    a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
    print a_dict
    a_dict['db'] = 'blog'
    print a_dict
 
    SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
                1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}
    print len(SUFFIXES)
    print 1000 in SUFFIXES
    print SUFFIXES[1000]
    print SUFFIXES[1024]
    print SUFFIXES[1000][3]




if __name__ == '__main__':

    is_it_true(1)
    is_it_true(-1)
    is_it_true(0) 
    is_it_true(0.1)
    is_it_true([])

    is_it_true(fractions.Fraction(1, 2))    
    is_it_true((1, 2 , 3))

    a_set = {1, 2}
    is_it_true(a_set)

    test_numeric();
    test_list()
    test_tuple()
    test_set()
    test_dict()
