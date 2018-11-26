import os
import random
import urllib.request

import requests
import hashlib
import json

import time
import xlrd
import xlwt

from ExcelUtil import excel_table_byname


requestCookie = '''
GET /webview/pingd?dm=taclick&pvi=968521518227125509&si=s45821518227932367&url=sign_in_email_signin_submit&arg=&ty=0&rdm=om.qq.com&rurl=/&rarg=&adt=&r2=500549930&r5=&scr=1467x825&scl=24-bit&lg=zh-cn&tz=-8&ext=version=2.0.6&random=1518228158239 HTTP/1.1
Host: pingtas.qq.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://om.qq.com/userAuth/index
Cookie: pgv_info=ssid=s7586965875; pgv_pvid=4437360156
Connection: keep-alive
'''



asdf = '''
GET /userAuth/randomCode?email=xdlc79%40163.com&relogin=1 HTTP/1.1
Host: om.qq.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Referer: https://om.qq.com/userAuth/index
X-Requested-With: XMLHttpRequest
Cookie: TSID=veqan87m0inhquhehsnnfq7c13; pgv_info=ssid=s7586965875; ts_last=om.qq.com/userAuth/index; pgv_pvid=4437360156; ts_uid=3364938942; OM_EMAIL=xdlc79@163.com; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; userid=6366243; alertclicked=%7C1%7C; rmod=1
Connection: keep-alive
'''


# ---------------------

# https://pingtas.qq.com/webview/pingd?dm=om.qq.com&pvi=391041518230262564&si=s64321518230262564&url=/userauth/index&arg=&ty=0&rdm=om.qq.com&rurl=/article/articlepublish&rarg=&adt=&r2=500549921&scr=1467x825&scl=24-bit&lg=zh-cn&tz=-8&ext=version=2.0.6&random=1518265257922

# https://pingfore.qq.com/pingd?dm=om.qq.com&url=/userAuth/index&rdm=om.qq.com&rurl=/article/articlePublish&rarg=-&pvid=9159124046&scr=1467x825&scl=24-bit&lang=zh-cn&java=0&pf=Win64&tz=-8&flash=-&ct=-&vs=tcss.3.1.5&ext=tm=1&hurlcn=&rand=74875&reserved1=-1&tt=

# https://pingtas.qq.com/webview/pingd?dm=taclick&pvi=391041518230262564&si=s64321518230262564&url=sign_in_email_signin_submit&arg=&ty=0&rdm=om.qq.com&rurl=/article/articlepublish&rarg=&adt=&r2=500549930&r5=&scr=1467x825&scl=24-bit&lg=zh-cn&tz=-8&ext=version=2.0.6&random=1518265531731