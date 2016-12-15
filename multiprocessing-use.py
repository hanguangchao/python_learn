# -*- coding: utf-8 -*-

import multiprocessing
import time
 

 
def func1(msg):
    for i in xrange(3):
        print msg
        time.sleep(1)


def func2(msg):
    for i in xrange(3):
        # print msg
        time.sleep(1)
    return "done " + msg


def test1():
    pool = multiprocessing.Pool(processes=4)
    for i in xrange(10):
        msg = "hello %d" %(i)
        pool.apply_async(func1, (msg, ))
    pool.close()
    pool.join()
    print "Sub-process(es) done.o"


def test2():
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(10):
        msg = "hello %d" %(i)
        result.append(pool.apply_async(func, (msg, )))
    pool.close()
    pool.join()
    for res in result:
        print res.get()
    print "Sub-process(es) done."


def test3():
    pool = multiprocessing.Pool(processes=4)
    result = {}
    for i in xrange(5):
        msg = "hello %d\n" %(i)

        result[i] = pool.apply_async(func2, (msg, ))
    pool.close()
    pool.join()
    for res in result:
        print res
    print "Sub-process(es) done."


if __name__ == "__main__":
   
    test3()
