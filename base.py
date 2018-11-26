import os
import time
import urllib

import requests
import hashlib
import json
import xlrd
import xlwt

useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
headers = {
    'User-Agent': useragent
}

Referer = "https://om.qq.com/userAuth/index"

def getFileMd5List(file, length):
    list = []
    while True:
        myhash = hashlib.md5()
        b = file.read(length)
        if not b :
            break
        myhash.update(b)
        dd = myhash.hexdigest()
        # print(dd)
        list.append(dd)
    return list

# myhash_md5 = hashlib.md5()
def getFileMd5ByName1(f):
    myhash = hashlib.md5()
    while True:
        b = f.read(1048576)
        if not b :
            break
        myhash.update(b)
    return myhash.hexdigest()

# myhash_sha1 = hashlib.sha1()
def getFileShaByName1(f):
    myhash = hashlib.sha1()
    while True:
        b = f.read(1048576)
        if not b :
            break
        myhash.update(b)
    return myhash.hexdigest()

if __name__ == '__main__':
    mm = getFileShaByName1("D:/py/weiboUploaderBase/videoBase/gdd559796@163.com/1 秒打出19拳，这就是道长独身50年练出的神手速.mp4")
    print (mm)

    newcat = "1+秒打出19拳，这就是道长独身50年练出的神手速"
    aaa = urllib.request.quote(newcat)
    print(aaa)

    res = requests.get("https://www.baidu.com/", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    })
    var = res.cookies

    for x in var:
        print(x)


