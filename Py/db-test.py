#/bin/sh python
# -*- encoding=utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import hashlib
import time, datetime

config = {
    'user' : 'homestead', 
    'host' : '127.0.0.1', 
    'port' : 3306, 
    'database' : "homestead", 
    'password' : "secret", 
    'use_unicode' : True
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# cursor.execute('select * from users where id = %s', ('1',))
cursor.execute('select * from users')
values = cursor.fetchall()
print values


try:
    insert_smt = (
        "INSERT INTO users (username, email, password, created_at)"
        " VALUES( %s, %s, %s, %s)"
    )
    m = hashlib.md5()
    m.update('123456')
    password = m.hexdigest()
    
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = ('python测试', 'python-test@han.cc', password, created_at)
    print insert_smt
    print data
    
    d = cursor.execute(insert_smt, data)
    print d
    
    id = cursor.lastrowid
    print 'last id:', id
    
    
    rr = cursor.execute(" INSERT INTO users (username, email, password, created_at) VALUES('python', 'python-test@han.cc', 'e10adc3949ba59abbe56e057f20f883e', '2016-07-26 09:23:31')")
    print rr

    id = cursor.lastrowid
    print 'last id:', id


    conn.commit()
    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    conn.rollback()
    print("Something went wrong: {}".format(err))





