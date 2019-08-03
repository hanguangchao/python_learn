#!/usr/bin/env python
# -*- coding=utf-8 -*-
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
print(today.__name__)



def log(*text):
     def decorator(func):
         def wrapper(*args,**kw):
             print("begin call %s %s()" % (text,func.__name__))
             try:
                 return func(*args,**kw)
             except:
                 print("error!")
             finally:
                 print("end call %s %s()" % (text,func.__name__))
         return wrapper
     if text != None:
         return decorator
     else:
         return wrapper
@log("execute")
def f():
     print("2016-7-24")

@log()
def f1():
     print("f1")

f()
f1()
