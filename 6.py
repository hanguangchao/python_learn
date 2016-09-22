# -*- coding=utf-8 -*-

def print_params(*params):
    print params


print_params(1, 2, 3)


def print_params2(name, *params):
    print name, params

print_params2('name1', 1, 2, 3, 4)
print_params2('name2')

def print_params3(name, **params):
    print params

print_params3('name3', x=1, y=2, c=3,)
print_params3('name3')

def print_params4(name, *pospar, **keypar):
    print name, pospar, keypar

print_params4('name4', 1, 2, 3, foo='a', bar='b')


x = 1 
def change_global():
    global x
    x = x + 1
change_global()
print x
