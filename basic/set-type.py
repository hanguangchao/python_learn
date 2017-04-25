# -*- coding:utf-8 -*-

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

"""
求两个集合的交集、差集
"""
valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])

print(input_set.intersection(valid))
print(input_set.difference(valid))

print(dir(set))

s = set()
s.add('a')
s.add('b')


print 'c' in s
s.update('d')
s.update('e')
print len(s)
print(s)
print(sorted(s))
print(sorted(s, reverse=True))

