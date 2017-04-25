# -*- coding: utf-8 -*- 
"""
Waits
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.get('https://www.lagou.com/zhaopin/houduankaifa/?labelWords=label')
try:
    element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "lg_header"))
            )
finally:
    driver.quit()

