# -*- coding=utf-8 -*-

"""
字符串
"""

from math import pi
print pi
print '"%10.6f"' % pi
print '%010f' % pi
print '%+10f' % pi
print '%-10f' % pi

print '"%-*s"' % (10, 'abc')

print '=' * 20

title = 'hello python , Hello World, Hello hello'
print title.find('python')
print title.find('H')
print title.find('h')

pos = title.find('h')
print pos

if (pos != -1):
    print "find h at %d" % pos



print title.count('h')
print title.rfind('hello')
print title.center(50, '=')


s = ['h', 'e', 'l', 'l', 'o']
ss = '-'.join(s)
print ss
print ss.split('-')



print title.lower()
print title.upper()
print title.capitalize()
print title.split(',')


print 'This is a test'.replace('is', 'eez')


print ' hello   '.strip()




