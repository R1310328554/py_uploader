import json
import http.cookiejar as HC
import logging
import os

import requests
from functools import partial
# from tengxun_tvu_starter import get_location_cookies


def loginFromCookie(session, email, location_cookies="cookies"):
    try:
        # srcSess = session.cookies
        # location_cookies = get_location_cookies();
        cookies_file_name = os.path.join(location_cookies, email + ".cookies.txt")
        cJar = HC.LWPCookieJar(filename=cookies_file_name)
        # for ind, cookie in enumerate(cJar):
        #     logging.info("%d ===  %s" % (ind, cookie))
        # cJar.clear()
        #  如果存在cookies文件，则加载，如果不存在则提示
        session.cookies = cJar
        session.cookies.load(ignore_discard=True)
        # session.cookies.get()
        # cJar.
        cJar.get = partial(func, cJar)
        # for ind, cookie in enumerate(cJar):
        #     logging.info("cookie序号:%d - 值:%s" % (ind, cookie))
            # print(cookie.name )
            # print(cookie.value   )
        logging.info(" === 成功从本地文件中加载cookie ！" + email)
        return True
    except Exception as e:
        logging.error('Err ' + str(e))
        # logging.error('未找到cookies文件 ?? ')
        # cJar.get = partial(func, cJar)
        return False

def markCookie(session, email, location_cookies="cookies"):
    # location_cookies = get_location_cookies();
    cookies_file_name = os.path.join(location_cookies, email + ".cookies.txt")
    if os.path.exists(cookies_file_name):
        os.remove(cookies_file_name)
    cJar = HC.LWPCookieJar(filename=cookies_file_name)

    cJar.get = partial(func, cJar)
    session.cookies = cJar
    logging.info("=== 准备将cookie 保存到本地文件中去 ！" + email)
    # cJar.save();


def test1():
    session = requests.session()
    markCookie(session, "lk@163.com")
    session.get("http://www.baidu.com")
    session.cookies.save()
    session.close()


def func(self, key):
    self.a = 2
    # print("key %s " % key)
    for ind, cookie in enumerate(self):
        # logging.info("cookie序号:%d - 值:%s" % (ind, cookie))
        if key == cookie.name:
            return cookie.value
    return None

def test2():
    session = requests.session()
    boo = loginFromCookie(session, "aaaxdlc79@163.com")

    if not boo:
        markCookie(session, "aaaxdlc79@163.com")

    key = "userid"
    cookies = session.cookies
    print(cookies)
    omtoken = cookies.get(key)
    print(omtoken)
    print("key:%s, value:%s" % (key, omtoken))

    cookies.save()
    session.close()


if __name__ == '__main__':
    test2()
