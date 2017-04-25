# -*- coding=utf-8 -*-


x, y, z = 1, 2, 3
print x, y, z


x, y = y, z
print x, y, z

values = 1, 2, 3
print values

x, y, z = values
print x
print x, y, z 

d = {'name' : 'a', 'friend': 'b'}
key , value = d.popitem()
print key, value


from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    print n, root, int(root)
    if root == int(root):
        print n
        break
else:
    print 'not found'



d1 = {'a':1, 'b':2}
d2 = d1
print d1, d2
d1 = None 
print d1
print d2 
d2 = None 
print d1, d2




