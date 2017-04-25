# -*- coding: utf-8 -*-



from selenium import webdriver
service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ] 

driver = webdriver.PhantomJS()
                          
driver.get("http://icanhazip.com")
print(driver.page_source) 
driver.close()
