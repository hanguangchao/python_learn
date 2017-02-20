# -*- coding: utf-8 -*- 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Chrome()
driver.set_window_size(1920, 1080)
driver.get('http://www.xcar.com.cn/')
time.sleep(10)

with open('/Users/han/tmp/xcar.html', 'w') as opened_file:
    opened_file.write(driver.page_source)
# 截图
driver.get_screenshot_as_file('/Users/han/tmp/xcar.png')
time.sleep(5)
driver.quit()
