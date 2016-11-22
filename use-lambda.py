# -*- coding=utf-8 -*_

add = lambda x, y: x + y

print(add(3,6))


a= [(1, 2), (4,5), (98,4), (-12, 100)]
a.sort(key = lambda x: x[1])
print(a)
