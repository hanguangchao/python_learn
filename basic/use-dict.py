# -*- coding=utf-8 -*-

"""
字典 
"""

l = [('key1', 'val1'), ('key2', 'val2')]
print dict(l)


d = {}.fromkeys(['a', 'b', 'c'])
print d
print {}.fromkeys(['a', 'b', 'a'])


print d.get('a', 'a default.')
print d.get('c')
print d.get('d')
print d.get('d', 'ddd')

print d.__str__()

print __name__
d1 = d.items()
print type(d1)
print list(d1)

d1 = d.iteritems()
print type(d1)
print list(d1)

d1 = d.iterkeys()
print list(d1)

d1 = d.itervalues()
print list(d1)

name = 'a'
txt = 'text'
print name, txt
