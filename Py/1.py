#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from collections import Iterable

alist = ['a', 'b', 'c']

for item in alist:
    print item

if 'a' in alist:
    print 'a in alist'
else:
    print 'a not in alist'


age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print my_abs(-1)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print isinstance('abc', Iterable)


for x, y in [(1, 11), (2, 22), (3, 33)]:
    print x, y


lista = ['a', 'b', 'c']
print len(lista)
lista.append('d')
print len(lista)

print 'lista contsns a? :::', lista.__contains__('a')
for x in lista:
    print 'list item :', x

print lista[-1]
print lista[-2]


t = (1,)

print 't isinstance tuple:', isinstance(t, tuple)

# 循环
sum = 0
for n in range(101):
    sum += n
print sum


# 计算100以内所有奇数的和

sum = 0
n = 99

while n > 0:
    sum += n
    n -= 2
print sum


'''
字典
'''


d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print d['Michael']


print d.viewkeys().__contains__('a')
print d.has_key('a')


# dict = {"a" : "apple", "b" : "grape"}
# dict2 = {"c" : "orange", "d" : "banana"}
# dict2 = dict.copy()
# print dict2

print '========================'


import copy
dict = {"a": "apple", "b": {"g": "grape", "o": "orange"}}
dict2 = copy.deepcopy(dict)
dict3 = copy.copy(dict)
dict2["b"]["g"] = "orange"
print dict
dict3["b"]["g"] = "orange"
print dict


print '========================'

# 查找2个字典的交集和并集 指的是键

dict1 = {1: 2, 2: 3, 3: 3}
dict2 = {1: 2, 4: 3, 3: 5}


# 交集
# for要用循环次数小的 可以提高性能
inter = dict.fromkeys([x for x in dict1 if x in dict2])
print inter


# set 并集
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print set1 | set2
print set1.union(set2)
# set 交集
set1 = {1, 2}
set2 = {1, 2, 3, 4}

print set1 & set2
print set1.intersection(set2)

print 'set:::::::::::::::::::::'
# set
s = set([1, 2, 3])

print s


'''
函数
'''


print int(12.34)
print float('123213.323')
print bool(0)
print bool('')


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


nums = [1, 2, 3]
print calc(nums)


def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


nums = [1, 2, 3]
print calc1(*nums)


'''
参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。


*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。


'''


def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw


func(1, 2)
func(1, 2, c=3)
func(1, 2, c=3, d=4)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)
func(1, 2, 3, 'a', 'b', x=99, y=1)


print '=' * 100


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print len(L)


L = range(101)

print L[:10]
print L[11:20]
print L[-10:]
print L[-10::2]

'''
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来

'''

print [x * x for x in range(1, 11)]

print [x * x for x in range(1, 11) if x % 2 == 0]


files_dirs = [d for d in os.listdir('.') if True == os.path.isdir(d)]
print files_dirs



from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling decorated function...')
        return func(*args, **kwargs)
    return wrapper  

@my_decorator 
def example():
    """Docstring""" 
    print('Called example function')

print(example.__name__, example.__doc__)

example()

