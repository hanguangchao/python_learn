# -*- coding: utf-8 -*- 
"""
Waits
"""
import sys
reload(sys)                         
sys.setdefaultencoding('utf-8')
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.set_window_size(1200,1000)
driver.get('http://bj.kongjianjia.com/xiezilou/1087')
time.sleep(1)
#js = """
#    console.log('js')
#    document.documentElement.scrollTop=10000;
#    document.body.scrollTop = 10000;
#"""
#driver.execute_script(js)
time.sleep(1)
print("模拟点击")
try:
    while (True): 
        elem = driver.find_element_by_id("lookmore")
        print(elem)
        elem.click()        
        time.sleep(1)
except:
    print("元素没找到")
    pass
time.sleep(1)
with open('/Users/han/tmp/1.html', 'w') as opened_file:
    opened_file.write(driver.page_source)
# 截图
driver.get_screenshot_as_file('/Users/han/tmp/1.png')
time.sleep(50)
driver.quit()
