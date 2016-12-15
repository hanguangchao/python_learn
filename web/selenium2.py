# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.get('http://baidu.com')

# 关闭标签页
driver.close()
# 关闭浏览器
driver.quit()
