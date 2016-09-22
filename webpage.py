# -*- coding=utf-8 -*-

from selenium import webdriver

browser = webdriver.PhantomJS()  #浏览器初始化；Win下需要设置phantomjs路径，linux下置空即可
url = 'http://www.zhidaow.com'  # 设置访问路径
browser.get(url)  # 打开网页
title = browser.find_elements_by_xpath('//h2')  # 用xpath获取元素

for t in title:  # 遍历输出
    print t.text # 输出其中文本
    print t.get_attribute('class')  # 输出属性值

browser.quit()  
