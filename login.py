import json
import logging

import requests
import hashlib
# from urllib import quote
from urllib.request import quote


# upqv97@163.com        qqq123qqq
# xdlc79@163.com   Pbv6zzBBX7ahLxK2V
# hrdt17@163.com   Pbv6zzBBX7ahLxK2V
# s = requests.Session( )
import cookielib_util


def saveCookie(email, cookie):
    pass


useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"

def login(sess, email, password, location_cookies):
    emailEnc = quote(email)
    # logging.info(emailEnc)

    try:
        found = cookielib_util.loginFromCookie(sess, email, location_cookies)
        # found = False;
        lastCookie = sess.cookies
        if found:
            r = sess.get('https://om.qq.com/')
            if len(r.history) == 1 and r.history[0].status_code == 302 and r.history[0].url == "https://om.qq.com/":
                logging.info("请求可能被重定向！")
                # sess.cookies.clear()
            if r.status_code == 200 and len(r.history) == 0:
                logging.info("从缓存中登录成功！" + email)
                return lastCookie
        cookielib_util.markCookie(sess, email, location_cookies)
    except Exception as e:
        # Can't convert 'FileNotFoundError' object to str implicitly
        logging.info(e)
        cookielib_util.markCookie(sess, email, location_cookies)

    r = sess.get('https://om.qq.com/userAuth/randomCode?email=' + emailEnc + '&relogin=1')
    # logging.info(r.headers)
    # logging.info(r.cookies)
    # logging.info(r.headers['content-type'])      application/json

    dic = eval(r.text)['data']
    # logging.info(dic)

    if len(dic ) == 0:
        logging.error(r.text)
        return
    token = dic['token']
    salt = dic['salt']

    md5 = hashlib.md5()
    md5.update((salt + password).encode("utf8"))
    pw = md5.hexdigest()
    md6 = hashlib.md5()
    md6.update((token + pw).encode("utf8"))
    pwd = md6.hexdigest()

    url = "https://om.qq.com/userAuth/SignIn?relogin=1"
    payload = {'email': email, 'pwd': pwd, 'tonken': token}
    # print(payload)

    headers = {
        'authority': 'om.qq.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://om.qq.com/userAuth/index',
        'User-Agent': useragent
    }

    try:
        r = sess.post(url, data=payload, headers=headers)
        if r.status_code == 200:
            logging.info(r.text)
            obj = r.json()
            code = obj["response"]["code"]
            msg = obj["response"]["msg"]
            if code == 0 and msg == "success":
                saveCookie(email, r.cookies)
                sess.cookies.save(ignore_discard=True, ignore_expires=True)

                # logging.info(" === 成功将cookie 保存到本地文件 ！" + email)
                logging.info("登录成功！" + email)
                return sess.cookies
        else:
            logging.error("无法登录成功： " + r.text)
    except Exception as e:
        logging.info(e)
        # return False

def loginxx(s, email, password):
    email = 'xdlc79@163.com'
    email = "upqv97@163.com"
    emailEnc = "upqv97%40163.com"

    password = 'Pbv6zzBBX7ahLxK2V'
    password = 'qqq123qqq'

    r = s.get('https://om.qq.com/userAuth/randomCode?email='+emailEnc+'&relogin=1')
    # logging.info(r.headers)
    # logging.info(r.cookies)
    logging.info(r.headers['content-type'])

    dic = eval(r.text)['data']
    token = dic['token']
    salt = dic['salt']

    md5 = hashlib.md5()
    md5.update((salt + password).encode("utf8"))
    pw = md5.hexdigest()
    md6 = hashlib.md5()
    md6.update((token + pw).encode("utf8"))
    pwd = md6.hexdigest()

    url = "https://om.qq.com/userAuth/SignIn?relogin=1"
    payload = {'email': email, 'pwd': pwd ,'tonken': token}
    # print (payload)

    headers = {
        'authority': 'om.qq.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, sdch, br',
        'accept-language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Referer': 'https://om.qq.com/userAuth/index',
        'User-Agent': useragent
    }

    r = s.post(url,data = payload, headers=headers )
    print (r.status_code)
    coo = r.cookies
    for k, v in coo.items():
        logging.info( "k " + k  + "   v " + v)
    # coo = json.loads(r.text)["data"]
    r.close()


    print (r.text)
    fimgurl = coo.get("fimgurl")
    logging.info(fimgurl)
    fname = coo.get("fname")
    logging.info(fname)
    cbvp = coo.get("cbvp")
    logging.info(cbvp)

    omtoken = coo.get("omtoken")
    omtoken_expire = coo.get("omtoken_expire")
    randomkey = coo.get("randomkey")
    TSID = coo.get("TSID")
    userid = coo.get("userid")
    alertclicked = coo.get("alertclicked")
    key_9e67236d07bdc7152e6e2b42b7f00f43 = coo.get("9e67236d07bdc7152e6e2b42b7f00f43")

    obj = {
        "omtoken" : omtoken,
        "omtoken_expire" : omtoken_expire,
        "randomkey" : randomkey,
        "TSID" : TSID,
        "userid" : userid,
        "9e67236d07bdc7152e6e2b42b7f00f43" : key_9e67236d07bdc7152e6e2b42b7f00f43,
    }


# https://om.qq.com/article/articlePublish

# https://om.qq.com/article/articlePublish#/!/view:article?typeName=multivideos

# 把 用户名和sessionId 的 cookie 存起来，下次先查看cookie， 如果没有过期，直接使用


# tables = excel_table_byname(file='account.xlsx',colnameindex=2)
# for row in tables:
#     logging.info(row)

# r = s.get("https://om.qq.com/article/articlePublish#/!/view:article?typeName=multivideos")
# logging.info(r.text)

# r = s.get("https://om.qq.com/VideoManager/VideoCatagory?relogin=1")
# logging.info(r.text)
