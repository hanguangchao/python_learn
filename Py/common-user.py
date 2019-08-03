# -*- encoding=utf-8 -*-


'''
Python 常用模块
'''

'''
list
'''
classmates = ['Michael', 'Bob', 'Tracy']

'''
tuple
'''

classmates = ('Michael', 'Bob', 'Tracy')


'''
dict
'''
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

'''
set
'''
s = set([1, 2, 3])


from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p


from collections import deque


q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

print q

for x in q:
    print x

print q


from collections import defaultdict

dd = defaultdict(lambda: 'N/A')

dd['key1'] = 'abc'


from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print d
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od

od = OrderedDict()

od['x'] = 'x'
od['a'] = 'a'
od['c'] = 'c'


print od.keys()


# import base64

# print base64.b64encode('binary\x00string')
# print base64.b64decode('YmluYXJ5AHN0cmluZw==')


# print base64.b64encode('abcdefg')
# print base64.b64decode('YWJjZGVmZw==')


# def b64decode_self(str):
#     return base64.b64decode(str+'='*(4-len(str)%4))


# print b64decode_self('YWJjZGVmZw==')


import struct


print 'ssss'

print struct.pack('>I', 10240099)
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')



import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()



md5 = hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()


import hashlib

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()




# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print n
    






from xml.parsers.expat import ParserCreate



class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)



L = []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
L.append(r'some & data')
L.append(r'</root>')
s = ''.join(L)


print s









from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')






