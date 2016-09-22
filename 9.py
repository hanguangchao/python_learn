# -*- coding=utf-8 -*-

def repeater(value):
    while True:
        new = (yield value)
        if new is not None: value = new

r = repeater(42)
print r.next()

print r.send("Hello World!")




def triangles():
    ls = []
    while True:
        ls.insert(0, 1)
        for k, v in enumerate(ls[1:-1], 1):
            ls[k] = v + ls[k + 1]
        yield ls


n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10:
        break


        
