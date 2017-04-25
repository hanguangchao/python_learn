# -*- coding:utf-8 -*-

import multiprocessing
import time
import os
import datetime



from mysql import SimpleMysql

def checkIp(ip):
    #print 'curl -x %s  www.baidu.com -m 5 --connect-timeout 5  -o /dev/null -s -w "%%{http_code}"' % (ip,)
    p = os.popen('curl -x %s  www.baidu.com -m 5 --connect-timeout 5  -o /dev/null -s -w "%%{http_code}"' % (ip,))
    http_code =  int(p.read().strip())
    if 200 == http_code:
        return True
    else:
        print ip, http_code
        return False


db = SimpleMysql(user='homestead', passwd='secret', db='webspider', host='192.168.10.10', charset="utf8", use_unicode=True)
proxylist = db.getAll(table='free_proxy_list',
        where = ("last_checked > %s AND checked_status = %s ", ["2016-11-15", "0"]),
        order = ('last_checked', 'DESC'),
        limit = (0, 100)
    )

print len(proxylist)

if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=20)
    result = {}

    checker_procs = []
    for x in proxylist:
        
        ip = "%s:%s" % (x.ip, x.port)
        # pool.apply_async(checkIp, (ip, ))
        # result.append(pool.apply_async(checkIp, (ip, )))
        result[x.id] = pool.apply_async(checkIp, (ip, )
    pool.close()
    pool.join() 
    for res in result:
        print res
        print res.get()
    print "Sub-process(es) done."



