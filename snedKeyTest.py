# -*- coding: utf-8 -*-
from selenium import webdriver
import win32gui
import win32con
import time

dr = webdriver.Firefox()
dr.get('http://sahitest.com/demo/php/fileUpload.htm')
upload = dr.find_element_by_id('file')
upload.click()
time.sleep(1)

# SendKeys
SendKeys.SendKeys('D:\\29.png')  # 发送文件地址
SendKeys.SendKeys("{ENTER}") # 发送回车键

print (upload.get_attribute('value'))
dr.quit()