from selenium import webdriver

import time

browser = webdriver.Chrome()

first_url = 'http://www.baidu.com'
browser.get(first_url)


sec_url = 'http://www.163.com'
browser.get(sec_url)

# browser.find_element_by_xpath('//div/div/div/ul/li[1]/strong/a').click()

browser.switch_to_window(browser.window_handles[0])

tt  = browser.title  # 第一个页面
print(tt)

browser.switch_to_window(browser.window_handles[1])

tt2 = browser.title  # 最后一个页面
print(tt2)

browser.quit()