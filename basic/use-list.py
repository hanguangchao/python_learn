# -*- coding=utf-8 -*-

'''
list
'''

mylist = [1, 2, 3]
mylist.append(4)
mylist.append([4, 5, 6])

print mylist


lista = [1, 2, 3]
lista[1] = 5
print lista

del lista[1]
# del lista[3]
print lista

# 分片赋值
l = list('Perl')
l[2:] = 'ar'
print l
l[1:] = 'ython'
print l

number = [1, 5]
number[1:1] = [2, 3, 4]
print number
number[1:4] = []
print number

"""
列表方法
list.append()
list.count()
list.extend()
"""

b = ['a', 'b', 'c', 'd', 'a', 'c', 'c']
b.append('f')
b.append(['g', 'h'])
b.append([1, 2, 3])
print b
print b.count('a')
print b.count('c')
print b.count('e')


a = [1, 2, 3]
b = [4, 5, 6]
print 'a::' , a
print 'a+b::', a+b 
print a.index(3)

c = [1, 2, 3]
d = [4, 5, 6]
c.extend(d)
print c

c.insert(3, 'aaa')
print c
c.insert(-1, 'ddd')
print c

c.pop()
print c

c.remove(1)
print c
c.reverse()
print c

x = [4, 6, 3 ,2,7, 5]
x.sort()
print x

print x[:]
y = x

print y
y.sort()
print y

z = sorted(x)
print z  


"""
元组
"""
print 1,
print (1,)
print 8*(1+2,)

x = [1, 2, 3]
y = tuple(x)
print x, y 




