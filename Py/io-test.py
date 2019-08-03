
try:
    f = open('/Users/han/Code/Py/2.py', 'r')
    print f.read()
finally:
    if f:
        f.close()

with open('1.py', 'r') as f:
    print f.read()



f = open('exception.py', 'r')
for line in f.readlines():
    print(line.strip())




import os

# print dir(os)



print os.getgroups()

print os.name
print os.getcwd()

print os.path.abspath('./')


# f = os.path.join(os.path.abspath('./'), 'testdir')
# print f

# os.mkdir(f)
# os.rmdir(f)


print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']





import json
d = dict(name='Bob', age=20, score=88)
j = json.dumps(d)
print j

print json.loads(j)



