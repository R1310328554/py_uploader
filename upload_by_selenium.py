import re
import time

import win32api
import win32con
import win32gui
from ctypes import *

import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions
import cookielib_util

import login
import win32guiTest


def getBySelenium(cookies, url):
    # 如果driver没加入环境变量中，那么就需要明确指定其路径
    # 验证于2017年4月11日
    # 直接登陆新浪微博
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.set_page_load_timeout(30)
    driver.get(url)
    for co in cookies:
        print(co)
        driver.add_cookie(co)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source # 新url 已经加载， 为什么 page_source 还没变化？
    print(page)


    # liElement = driver.find_element_by_xpath('//div[@class="tab-inline clearfix"]/li[@href="view:article?typeName=multivideos"]')
    # liElement.click()

    # liElement = driver.find_element_by_xpath('//div[@class="tab-inline clearfix"]/li[@href="view:article?typeName=multivideos"]')
    # liElement.click()
    # https://om.qq.com/article/articlePublish#/!/view:article?typeName=multivideos

    # liElement = driver.find_element_by_xpath('//div[@id="om-art-videos-index"]"]')
    # liElement = driver.find_element_by_xpath('//div[@class="uploadPlaceholder"]')
    # liElement = driver.find_element_by_xpath('//div[@id="om-art-videos-index"]/div[@class="upload-block upload-block-media action-upload"]/div[@class=uploadPlaceholder"]')
    liElement = driver.find_element_by_id("btn-upload-video")
    liElement.click()
    alert = driver.switch_to_alert()
    driver.switch_to_window()
    driver.switch_to_active_element()

    video = "C:\\Users\\Ada\\Documents\\Tencent Files\\1310328554\\FileRecv\\汽车\\aaaaa.mp4"
    video = "C:\\Users\\Ada\\Documents\\aa\\1.5T涡轮增压2017款本田crv百公里加速，仪表吊炸天.mp4"
    video = "C:\\Users\\Ada\\Documents\\aa\\3辆电动车同时闯红灯，其中一辆的结局令人惋惜.mp4"
    # video = "D:\\aaaaa.mp4"
    win32guiTest.clickUpload(video)
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//div[@class="form-group videocategory"]/div').click();
        windll.user32.SetCursorPos(566, 350);
        bb = driver.find_element_by_xpath('//ul[@class="group-result-list"]/li[contains(text(),"资讯")]');

        # builder.moveToElement(div1).perform(); // 元素位置
        # ActionChains(driver).move_to_element(bb).click(hidden_submenu).perform()

        driver.execute_script('window.scrollTo(0,800)')

        # bb = driver.find_element_by_xpath('//ul[@class="group-result-list"]/li[contains(text(),"汽车资讯")]');
        bb.click()
        time.sleep(1)
        cnt = 1
        while cnt < 5:
            cnt += 1;
            tag = driver.find_element_by_xpath('//ul[@class="form-tags-line titleVideoTags"]/li[%s]'%cnt)
            tag.click()

        time.sleep(1)
        time.sleep(1)
        time.sleep(1)
        publishXpath = '//*[@id="mod-actions"]/div/button'
        publish = driver.find_element_by_xpath(publishXpath)
        publish.click()


    except Exception as e:
        print(e)
        pass

    time.sleep(1)
    time.sleep(3999999)

if __name__ == '__main__':
    url = 'https://om.qq.com/userAuth/index'
    name_input = "ahsaln@163.com"     # input('请输入登录用户名：\n')
    passwd_input = "mzTSXnB4O62Mjng"     # input('请输入登录密码：\n')

    session = requests.session()
    location_cookies = "cookies"
    lastCookie = login.login(session, name_input, passwd_input, location_cookies)
    # found = cookielib_util.loginFromCookie(session, name_input)
    load_cookies = requests.utils.dict_from_cookiejar(session.cookies)

    print({c.name: c.value for c in session.cookies})

    load_cookies_list = []
    for k, v in load_cookies.items():
    # for k, v in load_cookies:
        print(k, v)
        newDict = {}
        newDict["name"] = k
        newDict["value"] = v
        load_cookies_list.append(newDict)
    # for i, header in enumerate(lastCookie.__dict__):
    #     print(i, header)

    articlePublish = "https://om.qq.com/article/articlePublish"
    articlePublish = "https://om.qq.com/article/articlePublish#/!/view:article?typeName=multivideos"
    getBySelenium(load_cookies_list, articlePublish)












