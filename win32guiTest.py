from selenium import webdriver
from selenium.webdriver import ChromeOptions

import win32gui
import win32con
import time


agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'
headers = {
    'User-Agent': agent
}

def test():
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--user-agent=%s'%agent)
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    dr = webdriver.Chrome(chrome_options=chrome_options)
    # dr = webdriver.Chrome()
    dr.get('http://sahitest.com/demo/php/fileUpload.htm')
    upload = dr.find_element_by_id('file')
    upload.click()
    time.sleep(1)

    # win32gui
    # dialog = win32gui.FindWindow('#32770', '打开')  # 对话框 chrome
    dialog = win32gui.FindWindow('#32770', '文件上传')  # 对话框 ff
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\BugReport.txt')  # 往输入框输入绝对地址
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    win32gui.PostMessage()

def clickUpload(file):
    # win32gui
    dialog = win32gui.FindWindow('#32770', '打开')  # 对话框 chrome
    # dialog = win32gui.FindWindow('#32770', '文件上传')  # 对话框 ff
    print("dialog", dialog)
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    print("ComboBoxEx32", ComboBoxEx32)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    print("ComboBox", ComboBox)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    print("Edit", Edit)
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    print("button", button)

    win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file)  # 往输入框输入绝对地址
    # win32gui.SendMessage(dialog, win32con.BM_CLICK, 1, button)  # 按button
    win32gui.PostMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button

    # time.sleep(10000)

if __name__ == '__main__':
    # test()
    clickUpload("D:\\BugReport.txt")