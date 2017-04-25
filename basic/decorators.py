# -*- coding: utf-8 -*-


def hi(name="abc"):
    return "hi " + name
print(hi())

greeting = hi
print(greeting())

del hi
print(greeting('cccc'))
'''NameError: name 'hi' is not defined'''
# print(hi())


def hii(name='default name'):
    print("now you are inside the hii() function")

    def greet():
        return "now you are inside the greet() function"
    def welcome():
        return "now you are inside the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hii()

# 上面展示了无论何时你调用hii(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如："


# greet()
# NameError: name 'greet' is not defined

"""
从函数中返回函数
"""
def hiii(name="a"):
    def greet():
        return "now you are in the greet() function"
    def welcome():
        return "now you are in the welcome() function"
    if name == "a":
        return greet
    else:
        return welcome

a = hiii()
print(a)
print(a())

"""
将函数作为参数传递给另一个函数
"""

def hill():
    return "hi yasoob"
def doSomethingBeforeHi(func):
    print("I am doing some")
    print(func())

doSomethingBeforeHi(hill)


"""
装饰器
"""

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doning some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some docoration to remove my foul smell")

a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()

print("%s" % "=" * 50)


@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
print(a_function_requiring_decoration)
print(a_function_requiring_decoration.__name__)



from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doning some boring work after executing a_func()")

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to remove my foul smell")

print(a_function_requiring_decoration.__name__)



print("="*50)
"""用装饰器实现log功能"""
from functools import wraps
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x

result = addition_func(1)
print(result)
print(addition_func.__name__)


print("="*50)
"""在函数中嵌入装饰器"""
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)

            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc1()
myfunc2()











