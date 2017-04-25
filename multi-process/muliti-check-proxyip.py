# -*- coding:utf-8 -*-

from multiprocessing import Process
import os

from mysql import SimpleMysql

def checkIp(ip):
   # print 'curl -x %s  www.baidu.com -m 5 --connect-timeout 5  -o /dev/null -s -w "%%{http_code}"' % (ip,)
    p = os.popen('curl -x %s  www.baidu.com -m 5 --connect-timeout 5  -o /dev/null -s -w "%%{http_code}"' % (ip,))
    http_code =  int(p.read().strip())
    if 200 == http_code:
        return True
    else:
        #print ip, http_code
        return False


db = SimpleMysql(user='homestead', passwd='secret', db='webspider', host='192.168.10.10', charset="utf8", use_unicode=True)
proxylist = db.getAll(table='free_proxy_list',
        where = ("last_checked > %s AND checked_status = %s ", ["2016-11-15", "0"]),
        order = ('last_checked', 'DESC'),
        limit = (0, 1000)
    )

print len(proxylist)



if __name__ == '__main__':



    checker_procs = []
    for x in proxylist:
        ip = "%s:%s" % (x.ip, x.port)
        
        proc = Process(target=checkIp, args=(ip,))
        checker_procs.append(proc)
        proc.start()

    for proc in checker_procs:
        proc.join()





