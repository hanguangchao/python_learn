#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys
"""
check proxy ip 
"""
def checkArg():
    if len(sys.argv) == 2:
        return True
    else:
        return False

def checkIp():
    if checkArg():
        ip = sys.argv[1]
        p = os.popen('curl -x %s  www.baidu.com -m 5 --connect-timeout 5  -o /dev/null -s -w "%%{http_code}"' % (ip,))
        http_code =  int(p.read().strip())
        if 200 == http_code:
            print "%s is good" % ip 
        else:
            print "%s is bad" % ip 
    else:
        print "required  ip:port "

if __name__ == '__main__':
    checkIp()
