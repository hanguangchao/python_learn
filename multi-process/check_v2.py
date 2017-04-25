# -*- coding:utf-8 -*-

import sys
import os

from mysql import SimpleMysql

import multiprocessing
import time
import requests
from datetime import datetime

db = SimpleMysql(user='homestead', passwd='secret', db='webspider', host='192.168.10.10', charset="utf8", use_unicode=True)


def date_now():
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def checkIp(ip, id):
    """
    proxy 数据库中的一条数据
    """
    # print("=============")
    # print(proxy)
    # ip = "%s:%s" % (proxy.ip, proxy.port)
    #p = os.popen('curl -x %s  www.baidu.com -m 3 --connect-timeout 3  -o /dev/null -s -w "%%{http_code}"' % (ip,))
    #http_code =  int(p.read().strip())

    proxies = {"http": "http://{proxy}".format(proxy=ip),
               "https": "https://{proxy}".format(proxy=ip)}
    #print(proxies)
    try:
        r = requests.get('http://www.baidu.com/', proxies=proxies, timeout=3, verify=False)
        if r.status_code == 200:
            db = SimpleMysql(user='homestead', passwd='secret', db='webspider', host='192.168.10.10', charset="utf8", use_unicode=True)
            db.update(table='free_proxy_list', data={ "checked_status": 1, "last_checked": date_now() }, where=("id=%s", [id,]) )
            db.commit()
            print "%s is good" % ip
        else:
            print "%s is bad" % ip
            db = SimpleMysql(user='homestead', passwd='secret', db='webspider', host='192.168.10.10', charset="utf8", use_unicode=True)
            db.update(table='free_proxy_list', data={ "checked_status": 0, "last_checked": date_now() }, where=("id=%s", [id,]))
            db.commit()
    except Exception as e:
        print "Exception"
        db = SimpleMysql(user='homestead', passwd='secret', db='webspider', host='192.168.10.10', charset="utf8", use_unicode=True)
        db.update(table='free_proxy_list', data={ "checked_status": 0, "last_checked": date_now() }, where=("id=%s", [id,]))
        db.commit()
        
    print db.lastQuery()

def multiCheckIp():
    """
    检查IP是否可用
    """
    date_where = "2016-10-10"
    db = SimpleMysql(user='homestead', passwd='secret', db='webspider', host='192.168.10.10', charset="utf8", use_unicode=True)
    proxylist = db.getAll(table='free_proxy_list',
        where = ("last_checked > %s AND checked_status = %s AND https = 'HTTP' ", [date_where, "0"]),
        order = ('id', 'DESC'),
        limit = (0, 500)
    )
    print db.lastQuery()
    if proxylist:
        try:
            #pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
            pool = multiprocessing.Pool(processes=50)
            for proxy in proxylist:
                ip = "%s:%s" % (proxy.ip, proxy.port)
                pool.apply_async(checkIp, (ip, proxy.id))
            pool.close()
            pool.join()
        except Exception as e:
            raise e
        finally:
            print 'All subprocesses done.'
            pass
    else:
        print("没有可用IP")

if __name__ == '__main__':
    multiCheckIp()
   
