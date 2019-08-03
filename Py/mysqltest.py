# -*- coding=utf-8 -*-
import MySQLdb
db=MySQLdb.connect(host="192.168.10.10", user="homestead", passwd="secret",db="webspider")
c = db.cursor()
c.execute("SET NAMES utf8")
c.execute("SELECT * FROM a1;")
print c.fetchall()


db.query("SELECT * FROM a1;")
# print db.fetchall()
