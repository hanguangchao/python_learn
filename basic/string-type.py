# -*- coding: utf-8 -*-

print "ABCDEFA:DE:EDE:E".split(":")

a_string = 'My alphabet starts where your alphabet ends.'
print a_string[3:13]
print a_string[3:-3]
print a_string[0:2]
print a_string[:18]
print a_string[18:]


s = '深入Python'
print len(s)

query = 'user=pilgrim&database=master&password=PapayaWhip'
alist = query.split('&')
print(alist)
alistlist = [ v.split('=') for v in alist]
print(alistlist)
adict = dict(alistlist)
print(adict)
