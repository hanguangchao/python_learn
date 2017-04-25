# -*- coding: utf-8 -*-
# python3 urllib
from urllib.request import urlopen

html = urlopen("http://pythonscraping.com/pages/page1.html") 
print(html.read())
