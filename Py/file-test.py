# -*- coding=utf-8 -*-

def testopen():
    f = open("1.py")
    for line in f:
        s = line.split(" ")
        print s 
    f.close()


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def testwith():
    with open(r'2.py') as somefile:
        for line in somefile:
            print line


if __name__ == '__main__':
    testwith()
