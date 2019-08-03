# -*- encoding=utf-8 -*-

import re


from collections import namedtuple

m = re.match(r'^(\d{3})-(\d{3,8})$', '132-12345', flags=0)
print m
print m.groups()



s = '1 2   3 4; 5--- 6'
print re.split(r'[\s\;\-]+', s)


print re.match(r'^(\d+)(0*)$', '102300').groups()
print re.match(r'^(\d+?)(0*)$', '102300').groups()

# <Tom Paris> tom@voyager.org

pattern = r'^(\<[\w\.\_\-\s]*?[^>]\>\s+)?([\w\.\_\-]+?)\@([\w\_\-]+?\.[\w\_\-]+[\w\_\.\-]*)$'


print re.match(pattern, '<Tom Paris> tom@voyager.org').groups()



# input = 'hello      &nbspabcworld;fdsafas'
# re.search(pattern, string, flags=0)
# #第一个参数是正则表达式，第二个参数是要替换成的内容，第三个参数是替换原字符串
# output = re.sub(r'&nbsp([a-z0-9]*?);', '\\1 ', input)
# print output


print re.sub('[abc]', 'o', 'Mark') 
print re.sub('([abc])', r'o', 'Mark') 




Circle = namedtuple('Circle', ['x', 'y', 'r'])


print Circle
p = Circle(1, 2 , 3)



