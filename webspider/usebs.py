# -*- coding: utf-8 -*-

"""
使用BeautifulSoup从HTML或XML文件中提取数据

beautifulsoup4 (4.5.3)
"""

import requests
from bs4 import BeautifulSoup


# html_doc = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html").text
html_doc = requests.get("http://www.php1024.com/").text
soup = BeautifulSoup(html_doc)
# 使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象,并能按照标准的缩进格式的结构输出:
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.p)

print(soup.find_all('a'))
print(soup.get_text())



soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html.parser")
tag = soup.b
print(tag)



html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
print(soup.head)
print(soup.title)
print(soup.body.b)
print(soup.contents)
print(soup.contents[0].name)
head_tag = soup.head
title_tag = head_tag.contents[0]
for child in title_tag.children:
    print(child)




css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print css_soup.p['class']
# ["body", "strikeout"]

css_soup = BeautifulSoup('<p class="body"></p>')
print css_soup.p['class']
# ["body"]
