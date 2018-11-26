from selenium import webdriver
from pyvirtualdisplay import Display

#配置无界面chrome用
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.set_window_size(800,600) #设置浏览器窗口的大小
driver.get("http://baidu.com")
driver.quit()