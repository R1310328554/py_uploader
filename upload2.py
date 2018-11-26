# -*- coding:utf-8 -*-

import hashlib
import json
import logging
import os
import time
import base
import urllib.request

import requests

from xmlUtil import read_xml_from_txt


############################## 获取登录信息 ##############################
# s = requests.Session( )
# email = 'xdlc79@163.com'
# email = "upqv97@163.com"
# emailEnc = "upqv97%40163.com"
#
# r = s.get('https://om.qq.com/userAuth/randomCode?email='+emailEnc+'&relogin=1')
# # logging.info(r.headers)
# # logging.info(r.cookies)
# dic = eval(r.text)['data']
# token = dic['token']
# salt = dic['salt']
#
# password = 'Pbv6zzBBX7ahLxK2V'
# password = 'qqq123qqq'
# md5 = hashlib.md5()
# md5.update((salt + password).encode("utf8"))
# pw = md5.hexdigest()
# md6 = hashlib.md5()
# md6.update((token + pw).encode("utf8"))
# pwd = md6.hexdigest()
#
# url = "https://om.qq.com/userAuth/SignIn?relogin=1"
# payload = {'email': email, 'pwd': pwd ,'tonken': token}
# # print (payload)
#
# headers = {
#     'authority': 'om.qq.com',
#     'accept': 'application/json, text/javascript, */*; q=0.01',
#     'accept-encoding': 'gzip, deflate, sdch, br',
#     'accept-language': 'zh-CN,zh;q=0.8',
#     'Cache-Control': 'max-age=0',
#     'Referer': 'https://om.qq.com/userAuth/index',
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
# }
#
# r = s.post(url,data = payload, headers=headers )
# print (r.status_code)
# coo = r.cookies
# for k, v in coo.items():
#     logging.info( "k " + k  + "   v " + v)
# # coo = json.loads(r.text)["data"]
#
# # print (r.text)
# fimgurl = coo.get("fimgurl")
# # logging.info(fimgurl)
# fname = coo.get("fname")
# # logging.info(fname)
# cbvp = coo.get("cbvp")
# # logging.info(cbvp)
#
# omtoken = coo.get("omtoken")
# omtoken_expire = coo.get("omtoken_expire")
# randomkey = coo.get("randomkey")
# TSID = coo.get("TSID")
# userid = coo.get("userid")
# alertclicked = coo.get("alertclicked")
# # 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D
# a32Key = "9e67236d07bdc7152e6e2b42b7f00f43"  #　来源于  signin
# # a32Value = "46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D"
# # a32Value = "7dfb7edaa6c952d6f4270a02e004a833dcd4c7c2a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366288%2522%253Bi%253A1%253Bs%253A14%253A%2522upqv97%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522upqv97%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634281172_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%259C%25A8%25E6%2597%2585%25E8%25A1%258C%25E8%25B7%25AF%25E4%25B8%258A%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366288%2522%253B%257D%257D"
# a32Value = coo.get(a32Key)

############################## 获取登录信息 ##############################
# open_uid = "6366243"

alertclicked = "%7C1%7C" #coo.get("alertclicked")
a32Key = "9e67236d07bdc7152e6e2b42b7f00f43"  #　来源于  signin

useragent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"

# def upload(r, userid, fimgurl, fname, cbvp ,omtoken,omtoken_expire,randomkey,TSID,a32Key,a32Value):
def upload(email, s, cookie, video_file,newcat, newsubcat,tags):
    local_file = video_file.name
    ind = local_file.rfind("\\", 0)
    file_name = local_file[ind+1:]
    ind2 = file_name.rfind(".", 0) # 如果没有后缀。。
    file_suffix = file_name[ind2+1:]
    file_name_no_suffix = file_name[0:ind2]
    size = str(os.path.getsize(local_file))

    userid = cookie.get("userid")
    fimgurl = cookie.get("fimgurl")
    # logging.info(fimgurl)
    fname = cookie.get("fname")
    # logging.info(fname)
    cbvp = cookie.get("cbvp")
    # logging.info(cbvp)
    omtoken = cookie.get("omtoken")
    omtoken_expire = cookie.get("omtoken_expire")
    randomkey = cookie.get("randomkey")
    TSID = cookie.get("TSID")
    alertclicked = cookie.get("alertclicked")
    a32Value = cookie.get(a32Key)

    logging.info("=========================== 准备上传文件:%s, userid:%s, omtoken:%s, omtoken_expire:%s  " %(file_name, userid, omtoken, omtoken_expire))

    open_uid = userid
    mediaid = open_uid

    open_token = omtoken
    # omtoken_expire = "1518196588"
    # omtoken_expire = "1518265104"

    # TSID = "vb41d3d91l334h56kqo18p26q1" # piskuncs6vcic0kied13u0rii1
    # TSID = "gmesbdl5dp84ssdlco8c074kv3"
    # TSID = "ldc8ekhb24fjqrmfm6jc3u3t21"
    # TSID = "fhqku8mk2j3eqeem0im18f0l95"

    # fimgurl = "http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0"
    # fname = "%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85"

    uin="o0514870968"
    ts_uid="3971416064"
    uid="640f64f657fa1fb3" # xxx

    # omtoken = "c5569aeb61"
    # omtoken = "50be350c9c"

    # origframe = "delete.avi"

    fid = ""
    vid = ""
    # email = "xdlc79@163.com"
    # emailEncoded = "xdlc79&40163.com"
    # email = "xdlc79&40163.com"
    # email = "fi6956@163.com"
    # email = "upqv97%40163.com"
    #   upqv97@163.com----qqq123qqq

    pgv_pvi = "391041518230262564" # 本地存储 ， 这个参数不是每次都会附带 39104 1518230262564
    pgv_pvi = "9051836416" # 本地存储 ， 这个参数不是每次都会附带 39104 1518230262564
    pgv_si = "s6626417664" # 会话存储 ， 这个参数不是每次都会附带 s6432 1518230262564
    pgv_pvid = "623613877"

    r = s.get("https://pingfore.qq.com/pingd?dm=om.qq.com&url=/userAuth/index&rdm=om.qq.com&rurl=/data/index&rarg=-&pvid="+pgv_pvid+"&scr=1467x825&scl=24-bit&lang=zh-cn&java=0&pf=Win64&tz=-8&flash=-&ct=-&vs=tcss.3.1.5&ext=tm%3D1&hurlcn=&rand=88746&reserved1=-1&tt=")
    r = s.get("https://pingtas.qq.com/webview/pingd?dm=taclick&pvi=714581518355265759&si=s902171518550888644&url=video_publish_video_publish_uploadvideo&arg=&ty=0&rdm=om.qq.com&rurl=/article/videomanage&rarg=&adt=&r2=500549930&r5=&scr=1366x768&scl=24-bit&lg=zh-cn&tz=-8&ext=version=2.0.6&random=1518609693391")
    r = s.get("https://pingfore.qq.com/pingd?dm=om.qq.com&url=/userAuth/index&rdm=om.qq.com&rurl=/data/index&rarg=-&pvid="+pgv_pvid+"&scr=1467x825&scl=24-bit&lang=zh-cn&java=0&pf=Win64&tz=-8&flash=-&ct=-&vs=tcss.3.1.5&ext=tm%3D1&hurlcn=&rand=88746&reserved1=-1&tt=")

    # pgv_pvid = "4618129525"
    pgv_info = "ssid=s2532228369"
    pgv_info = "ssid=s3368838360"
    pt2gguin = uin
    o_cookie = "743392069"
    ts_last = "om.qq.com/article/articleManage"
    sid="CG3h0aZKftVIIy_qVC1uR1-DjsGllRFDMW8_6-Hoto2T1fkWozweXm3toGk9ypuq"
    csrfToken="omfPyrf_LBmM3bpMrsYmPYfk"

    uin = "0"

    ptcz = "f6a7f98cc4db828bf43c8d66135b4275959740a26deb6df9e661ed54ecfc9af0"
    RK = "TjtTSvs+f6"
    pac_uaaidaa = ""
    pac_uid = "1_743392069"
    tvfe_boss_uuid = "69f7405aadb81e4f" # cookie ， 这个参数不是每次都会附带
    tvfe_boss_uuid = "e50b603d39b6d378"

    relogin = "?relogin=1'"
    relogin = ""
    relogin2 = "&relogin=1"

    # local_file = "C:\\Windows\\winsxs\\amd64_microsoft-windows-tabletpc-inputpanel_31bf3856ad364e35_6.1.7601.17514_none_6fb51b358e21d75f\\delete.avi"
    # local_file = "C:\\Program Files\\Common Files\\Microsoft Shared\\ink\\FlickAnimation.avi"
    # local_file = "C:\\Windows\\winsxs\\amd64_microsoft-windows-tabletpc-inputpanel_31bf3856ad364e35_6.1.7601.23187_none_6ff5d25ca775c844\\correct.avi"

    starttime = time.time()
    # tick = str(int(starttime * 1000))
    # logging.info("file_name, size, tick  are : %s %s %s ", file_name, size, tick)

    # 13726942547	a7758730	车主聊车	汽车	2

    # 9e67236d07bdc7152e6e2b42b7f00f43 =
    # fname='+fname+'; fimgurl='+fimgurl+'

    headers = {
        'Host': 'om.qq.com',
        'User-Agent': useragent,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://om.qq.com/article/articlePublish',
        'X-Requested-With': 'XMLHttpRequest',
        #'Cookie': 'pgv_pvi='+pgv_pvi+'; pt2gguin='+pt2gguin+'; RK='+RK+'; ptcz='+ptcz+'; pgv_pvid='+pgv_pvid+'; o_cookie='+o_cookie+'; pac_uid='+pac_uid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL='+email+'; userid='+userid+'; uin='+uin+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; tvfe_boss_uuid='+tvfe_boss_uuid+'; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last='+ts_last+'; '+a32Key+'='+a32Value+'',
        'Cookie': 'pgv_pvi='+pgv_pvi+'; pgv_pvid='+pgv_pvid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL='+email+'; userid='+userid+'; uin='+uin+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last='+ts_last+'; '+a32Key+'='+a32Value+'',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }

    r = s.get('https://om.qq.com/VideoManager/VideoCatagory'+relogin,headers=headers)
    # logging.info(r)
    # logging.info(r.text)
    # logging.info(r.encoding)
    # logging.info(r.headers)
    # logging.info(r.cookies)
    TSID = str(r.cookies.get("TSID"))
    # logging.info(" TSID %s " % TSID)

    headers = {
        'Host': 'om.qq.com',
        'User-Agent': useragent,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Referer': 'https://om.qq.com/article/articlePublish',
        'X-Requested-With': 'XMLHttpRequest',
        #'Cookie': 'pgv_pvi='+pgv_pvi+'; pt2gguin='+pt2gguin+'; RK='+RK+'; ptcz='+ptcz+'; pgv_pvid='+pgv_pvid+'; o_cookie='+o_cookie+'; pac_uid='+pac_uid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL='+email+'; userid='+userid+'; uin='+uin+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; tvfe_boss_uuid='+tvfe_boss_uuid+'; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last='+ts_last+'; '+a32Key+'='+a32Value+'',
        'Cookie': 'pgv_pvi='+pgv_pvi+'; pgv_pvid='+pgv_pvid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL='+email+'; userid='+userid+'; uin='+uin+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last='+ts_last+'; '+a32Key+'='+a32Value+'',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }
    #Cookie: pgv_pvi='+pgv_pvi+'; pt2gguin='+pt2gguin+'; RK='+RK+'; ptcz='+ptcz+'; pgv_pvid='+pgv_pvid+'; o_cookie='+o_cookie+'; pac_uid='+pac_uid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL=xdlc79@163.com; userid=6366243; uin='+uin+'; tvfe_boss_uuid='+tvfe_boss_uuid+'; TSID=vt0mrvibu9nkses08ahts187f5; pgv_si=s2021468160; ts_refer=kf.om.qq.com/search; fname='+fname+'; fimgurl='+fimgurl+'; omtoken=c5569aeb61; omtoken_expire=1518196588; alertclicked=%7C1%7C; rmod=1; ts_last='+ts_last+'; '+a32Key+'='+a32Value+'
    # s = requests.Session()


    # TSID = str(r.cookies.get("TSID"))
    # logging.info(" TSID %s " % TSID)

    videa_md5 = base.getFileMd5ByName1(local_file)
    videa_sha1 = base.getFileShaByName1(local_file)
    # postdata = "qzreferrer=https%3A%2F%2Fom.qq.com%2Farticle%2FarticlePublish%23%2F%21%2Fview%3Aarticle%3FtypeName%3Dmultivideos&vid=&bid=open_omg_video&type=24&tags=&cat=&act=&title=&folder=&orifname="+file_name+"&size="+size+"&uptype=3&key=&open_uid="+open_uid+"&open_token="+open_token+"&uin=0&encuin=&g_tk=&otype=json"
    postdata = {
        "qzreferrer": "https://om.qq.com/article/articlePublish#/!/view:article?typeName=multivideos",
        "vid": "",
        "bid":"open_omg_video",
        "type": "24",
        "platform": "web",
        "tags": "",
        "cat": "",
        "act": "",
        "desc": "",
        "title": "",
        "folder": "",
        "orifname": file_name,
        "size": size,
        "uptype": 4,
        "sha": videa_sha1,
        "md5": videa_md5,
        "key":"",
        "addrtype":1,
        "open_uid":open_uid,
        "open_token":open_token,
        "uin": "0",
        "encuin": "",
        "g_tk": "",
        "otype":"json",
    }
    # lee = len(str(postdata))
    # logging.info(" leee  %s "  % lee)

    # aa = 1/0
    # Cookie: pgv_pvi='+pgv_pvi+'; pt2gguin='+pt2gguin+'; RK='+RK+'; ptcz='+ptcz+'; pgv_pvid='+pgv_pvid+'; o_cookie='+o_cookie+'; pac_uid='+pac_uid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL=xdlc79@163.com; userid=6366243; uin='+uin+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken=feb0596663; omtoken_expire=1518177382; rmod=1; tvfe_boss_uuid='+tvfe_boss_uuid+'; TSID=piskuncs6vcic0kied13u0rii1; alertclicked=%7C1%7C; ts_last='+ts_last+'; '+a32Key+'='+a32Value+'
    headers = {
        'Host': 'om.qq.com',
        'User-Agent': useragent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Content-Length': str(lee),
        'Referer': 'https://om.qq.com/article/articlePublish',
        # 'Cookie': 'pgv_pvi='+pgv_pvi+'; pt2gguin='+pt2gguin+'; RK='+RK+'; ptcz='+ptcz+'; pgv_pvid='+pgv_pvid+'; o_cookie='+o_cookie+'; pac_uid='+pac_uid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL='+email+'; userid='+userid+'; uin='+uin+'; tvfe_boss_uuid='+tvfe_boss_uuid+'; TSID='+TSID+'; ts_last='+ts_last+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; alertclicked=%7C1%7C; rmod=1; '+a32Key+'='+a32Value+'',
        'Cookie': 'pgv_pvi='+pgv_pvi+'; pgv_pvid='+pgv_pvid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL='+email+'; userid='+userid+'; uin='+uin+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last='+ts_last+'; '+a32Key+'='+a32Value+'',
        'Referer': 'https://om.qq.com/article/articlePublish',
        'Upgrade-Insecure-Requests': '1',
    }
    logging.info("开始上传 ... ")
    r = s.post('https://om.qq.com/VideoUpload/UnFtnReady?g_tk=',data=postdata, headers=headers)
    # logging.info(r.status_code)
    # logging.info(r.text)
    ## logging.info(r.cookies)

    indexStr = "frameElement.callback("
    ind1 = r.text.find(indexStr)
    ind2 = r.text.find("});")
    if ind2 > ind1 > 0:
        callbackJsonStr = r.text[ind1 + len(indexStr): ind2 + 1]
        #logging.info(callbackJsonStr)
        callbackJson = json.loads(callbackJsonStr)
        #json.dumps(callbackJson)
        # logging.info(type(callbackJson))

        UnFtnReady_TSID = str(r.cookies.get("TSID"))
        # logging.info(" UnFtnReady_TSID %s " % UnFtnReady_TSID)

        if "vid" in callbackJson:
            logging.info(" vid == " + callbackJson["vid"])
            vid = callbackJson["vid"]
        if "fid" in callbackJson:
            logging.info(" fid == " + callbackJson["fid"])
            fid = callbackJson["fid"]
        if "uin" in callbackJson:
            logging.info(" uin == " + str(callbackJson["uin"]))
            # uin = callbackJson["uin"]
            # uin = str(uin)
            # pass
    else:
        logging.error(" 上传失败 UnFtnReady ==>  "  + r.text)
        return 1, -1
    ### r.close()

    r = s.get('https://om.qq.com/VideoManager/GetUserTags?title=' + file_name_no_suffix + relogin2, headers=headers)
    # logging.info(r.text)
    jsonRst = r.json()
    recommend_tags = jsonRst["data"]["recommend_tags"]

    if len(recommend_tags) >= 5:
        tagsList = recommend_tags[0:5]
    else:
        tagsList = tags.split(",")
    encodedtags = "+".join(list(map(lambda x:urllib.request.quote(x.strip(" ")), tagsList)))


    time.sleep(1)


    headers = {
        'Host': 'uu.video.qq.com',
        'User-Agent': useragent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Access-Control-Request-Method': 'POST',
        'Connection': 'keep-alive',
        'Origin': 'https://om.qq.com',
    }
    uploadurl = 'https://uu.video.qq.com/v1/openvupvideo?g_tk='
    r = s.options(uploadurl, headers=headers)

    file_name_encodedaa = "temp_file_name_" + str(int(time.time() * 1000))
    postdata = {
        "fid": fid,
        "vid": vid,
        "bid":"open_omg_video",
        "type": "24",
        "tags": "",
        "cat": "",
        "act": "",
        "title": "",
        "folder": "",
        "fsize": size,
        "opt":7,
        "otype":"json",
        "open_uid":open_uid,
        "open_token":open_token,
        "uin": 0,
        "g_tk": "",
        "Filename": file_name_encodedaa,
    }


    files = [('Filedata', (file_name_encodedaa, video_file, 'video/' + file_suffix))]


    bound = "4021056925725";
    headers = {
        'Host': 'uu.video.qq.com',
        'User-Agent': useragent,
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        # 'Content-Type': 'multipart/form-data;charset=iso8859-1', #
        # 'Content-Type': 'multipart/form-data; boundary=---------------------------'+bound,
        # 'Content-Length': size,
        'Origin': 'https://om.qq.com',
        'Referer': 'https://om.qq.com/article/articlePublish',
        'Upgrade-Insecure-Requests': '1',
    }
    # uploadurl = 'http://localhost:8080/servvv'
    logging.info("上传中 ... " + file_name)

    # headers['content-type'] = 'charset=iso8859-1'
    r = s.post(uploadurl, data=postdata, headers=headers, files=files)
    # eee = r.encoding
    # print(eee)
    # return



    # postdata["Filedata"] = (file_name, video_file, 'video/avi')
    # with open('massive-body') as f:
    # r = requests.post(uploadurl, data=postdata, headers=headers)

    if r.status_code != 200:
        logging.error(" 上传失败 ==>  " + r.text)
        return 2,vid
    else:
        try:
            # jsonRst = r.json()
            # if jsonRst.
            QZOutputJson = str(r.text)
            if QZOutputJson.startswith("QZOutputJson="):
                if QZOutputJson == '''QZOutputJson={"em":-2105,"s":"f"};''':
                    logging.error(" 上传可能失败 ==>  " + r.text)
                    # file_name = file_name.encode().decode(encoding="gb2312", errors="ignore")
                    # print(file_name)
                    # postdata["Filename"] = file_name
                    # files = [('Filedata', (file_name, video_file, 'video/' + file_suffix))]
                    # # uploadurl = 'http://localhost:8080/servvv'
                    # logging.info("再次上传中 ... ")
                    # r = s.post(uploadurl, data=postdata, headers=headers, files=files)
                    # eee = r.encoding
                    # print(eee)
                    # print(r.text)
                    # if r.status_code != 200:
                    #     logging.info(" 上传失败 ==>  " + r.text)
                    #     return
                    # else:
                    #     # jsonRst = r.json()
                    #     # if jsonRst.
                    #     if str(r.text).find("-2105") > -1:
                    #         logging.info(" 上传可能失败 ==>  " + r.text)
                    #         return
                    return 2,vid
                else:
                    logging.info("上传可能成功 : " + r.text)
                    vid = json.loads(QZOutputJson[len("QZOutputJson="):-1])["vid"]
            else:
                logging.info(" 上传返回: " + QZOutputJson)
                vid = read_xml_from_txt(QZOutputJson)
        except Exception as e:
            logging.error(e)
            return 2,vid
            # pass

    ### r.close()
    # time.sleep(10)
    # 没有cookie 发送, 也没有cookie 返回
    # logging.info(r.cookies)
    # TSID = str(r.cookies.get("TSID"))
    # logging.info(" TSID %s " % TSID)


    # gmtime = time.gmtime()
    # logging.info(gmtime)
    finishedtime = time.time()
    # logging.info(finishedtime)

    timeconsume = int((finishedtime - starttime) * 1000)
    logging.info("上传耗时(ms) ： %i " % timeconsume)

    time.sleep(1)

    postdata = {
        "desc": "视频上传",
        "errorcode":0,
        "errormsg":"上传成功",
        "interface":"upload",
        "machineinfo":{"system":"win7","browser":"firefox","navigar": useragent,"flashver":27,"cookie":"开启","javascript":"开启","localstorage":"开启"},
        "params":{"mediaid": mediaid},
        "reponse":"{}",
        "timeconsume":timeconsume,
        "vid":vid
    }
    headers = {
        'Host': 'om.qq.com',
        'User-Agent': useragent,
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Content-Length': '556',
        # 'Content-Length': str(len(str(postdata))),
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://om.qq.com/article/articlePublish',
        'Cookie': 'pgv_pvi='+pgv_pvi+'; pgv_pvid='+pgv_pvid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL='+email+'; userid='+userid+'; uin='+uin+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; TSID='+UnFtnReady_TSID+'; alertclicked=%7C1%7C; ts_last='+ts_last+'; '+a32Key+'='+a32Value+'',
        # 'Cookie': 'pgv_pvi='+pgv_pvi+'; pt2gguin='+pt2gguin+'; RK='+RK+'; ptcz='+ptcz+'; pgv_pvid='+pgv_pvid+'; o_cookie='+o_cookie+'; pac_uid='+pac_uid+'; pgv_info='+pgv_info+'; ts_uid='+ts_uid+'; OM_EMAIL='+email+'; userid='+userid+'; uin='+uin+'; tvfe_boss_uuid='+tvfe_boss_uuid+'; TSID='+TSID+'; ts_last='+ts_last+'; fname='+fname+'; fimgurl='+fimgurl+'; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; alertclicked=%7C1%7C; rmod=1; '+a32Key+'='+a32Value+'',
    }

    logging.info("")
    # logging.info("last step to finish ! ")
    logging.info("确认上传 ... ")
    r = s.post('https://om.qq.com/videoUpload/Finished'+relogin,data=postdata, headers=headers)

    logging.info("确认上传result  " + r.text)
    if r.status_code != 200:
        logging.error(" 确认上传失败 ==>  " + file_name)
        return 3,vid
    else:
        jsonRst = r.json()
        code = jsonRst["response"]["code"]
        msg = jsonRst["response"]["msg"]
        if code != 0:
            logging.error("确认上传失败！" + file_name)
            return 3,vid
        else:
            logging.info(" 确认上传成功 ！")
    # logging.info(r.cookies)
    TSID = str(r.cookies.get("TSID"))
    logging.info(local_file + " => 上传成功 !  "  +  " TSID %s " % TSID)
    ### r.close()

    # return userid, vid, fid, file_name, timeconsume, UnFtnReady_TSID


    #  发布文件

    title = file_name_no_suffix
    # title = "2018测试上传" + file_name
    # tags = "test_tags+aaa+bbb"


    desc = ""
    # newcat = "电影"
    # newsubcat = "电影周边"
    fileType = "video"
    duration = "0:00:00 "

    headers = {
        'Host': 'om.qq.com',
        'User-Agent': useragent,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Cookie': 'pgv_pvi=4977534976; pt2gguin=o0743392069; RK=1XYB4IoBV0; ptcz=c227ecbaa2db628758b51fc0db013f8af3e80ff0fb05bead8fde1689fbe055d8; pgv_pvid=3316797086; o_cookie=743392069; pac_uid=1_743392069; pgv_info=ssid=s4110512380; ts_uid=6537587375; OM_EMAIL='+emailEncoded+'; userid='+userid+'; uin='+uin+'; uid='+uid+'; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; tvfe_boss_uuid=69f7405aadb81e4f; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last=om.qq.com/article/syncWeixin; 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }
        # Cookie: pgv_pvi=4977534976; pt2gguin=o0743392069; RK=1XYB4IoBV0; ptcz=c227ecbaa2db628758b51fc0db013f8af3e80ff0fb05bead8fde1689fbe055d8; pgv_pvid=3316797086; o_cookie=743392069; pac_uid=1_743392069; pgv_info=ssid=s4110512380; ts_uid=6537587375; OM_EMAIL=xdlc79@163.com; userid=6366243; uin=o0743392069; uid=753181314; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; TSID=75hqs61fipn55l50k0trq3luk1; omtoken=548c8ad189; omtoken_expire=1518071140; rmod=1; ts_last=om.qq.com/article/syncWeixin; tvfe_boss_uuid=69f7405aadb81e4f; alertclicked=%7C1%7C; 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D

    r = s.get('https://om.qq.com/videoManager/checkVideoParam?title='+title+'&tags='+tags+'&desc='+desc+'&relogin=1', headers=headers)
    ## logging.info(r.status_code)
    logging.info(r.text)
    # logging.info(r.cookies)

    jsonRst = r.json() # 验证通过， 正常返回是： {"response":{"code":0,"msg":"suc"},"data":null}
    code = jsonRst["response"]["code"]
    msg = jsonRst["response"]["msg"] # 验证成功是 succ
    # new_TSID = ""
    if code != 0:
        logging.info("验证失败！" + msg)
        return 4,vid
    else:
        logging.info("验证成功 ！" + msg)
        UnFtnReady_TSID = str(r.cookies.get("TSID"))
    time.sleep(1)

    changeParamUrl = "https://om.qq.com/videoManager/checkVideoParam?title="+title+"&tags="+tags+"&desc=&relogin=1"
    r = s.post(changeParamUrl)
    ## logging.info(r.status_code)
    logging.info(r.text)
    ## logging.info(r.cookies)
    time.sleep(1)
    jsonRst = r.json()
    code = jsonRst["response"]["code"]
    msg = jsonRst["response"]["msg"]
    if code != 0:
        logging.info("checkVideoParam失败！" + msg)
        return 5,vid
    else:
        logging.info("checkVideoParam成功 ！" + msg)
        TSID = str(r.cookies.get("TSID"))
        logging.info(local_file + " => checkVideoParam成功 !  "  +  " TSID %s " % TSID)
        ### r.close()
    # else:
    #     return jsonRst

    loop = 0;
    while(loop < 20):
        time.sleep(3)
        r = s.head("https://puap.qpic.cn/vpic/0/"+vid+"_fast_5.jpg/0?t=" + str(loop))
        loop = loop + 1
        status_code = r.status_code
        # print(status_code)
        if status_code == 200:
            logging.info(" _fast_5.jpg 生成ok ！" + str(loop))
            break

    if loop >= 20:
        return 5,vid
		
    # title = urllib.request.quote(title)
    # newcat = urllib.request.quote(newcat)
    # newsubcat = urllib.request.quote(newsubcat)
    # tags = urllib.request.quote(tags)

    # articles =	[{"vid":vid,"title":title,"is_commercial":0,"user_original":0,"user_vr":0,"commodity":"","apply_push_flag":0,"activity":"","cover_type":"","type":"56","content":"<p><iframe+allowfullscreen=\"\"+f=\"no\"+frameborder=\"0\"+height=\"270\"+src=\"//v.qq.com/iframe/preview.html?vid="+vid+"&amp;width=480&amp;height=270&amp;auto=0\"+type=\"video\"+width=\"480\"></iframe></p>","video":"{\"vid\":\""+vid+"\",\"title\":\""+title+"\",\"type\":\""+fileType+"\",\"desc\":\""+desc+"\",\"duration\":\""+duration+"\",\"img\":{}}","needpub":1}]
    # videos =	[{"title":title,"tags":tags,"desc":desc,"newcat":newcat,"newsubcat":newsubcat,"apply_video_origialFlag":0,"activity":"","vid":vid,"imgurl":"http://puap.qpic.cn/vpic/0/"+vid+"_fast_5.jpg/0","user_original":0,"tagsid":"{}","apply_video_originalFlag":0,"apply_video_vrFlag":0,"user_vr":0,"is_commercial":0,"commodity":"","apply_push_flag":0,"needpub":1,"uid":uid,"imgurlsrc":"system"}]
    #
    # articles_dumps = json.dumps(articles, ensure_ascii=False)
    # articles_dumps = urllib.request.quote(articles_dumps, safe="")
    # videos_dumps = json.dumps(videos, ensure_ascii=False)
    # videos_dumps = urllib.request.quote(videos_dumps, safe="")
    # data = "article=" + articles_dumps + "&" + "videos=" + videos_dumps
    # logging.info(" data ！" + data)

    # data = 'videos=[{"title":"'+ title +'","tags":"'+ tags +'","desc":"","newcat":"'+ newcat +'","newsubcat":"'+ newsubcat +'","apply_video_origialFlag":0,"activity":"","vid":"'+ vid +'","imgurl":"http://puap.qpic.cn/vpic/0/'+ vid +'_fast_5.jpg/0","user_original":0,"tagsid":"{}","apply_video_originalFlag":0,"apply_video_vrFlag":0,"user_vr":0,"is_commercial":0,"commodity":"","apply_push_flag":0,"needpub":1,"uid":"cbd0cad84ca17a2c","imgurlsrc":"system"}]&articles=[{"vid":"'+ vid +'","title":"'+ title +'","is_commercial":0,"user_original":0,"user_vr":0,"commodity":"","apply_push_flag":0,"activity":"","cover_type":"","type":"56","content":"<p><iframe+allowfullscreen=\"\"+f=\"no\"+frameborder=\"0\"+height=\"270\"+src=\"//v.qq.com/iframe/preview.html?vid='+ vid +'&amp;width=480&amp;height=270&amp;auto=0\"+type=\"video\"+width=\"480\"></iframe></p>","video":"{\"vid\":\"'+ vid +'\",\"title\":\"'+ title +'\",\"type\":\"video\",\"desc\":\"\",\"duration\":\"0:00:00\",\"img\":{}}","needpub":1}]'
    data = '''videos=%5B%7B%22title%22%3A%22ttttt%22%2C%22tags%22%3A%22aaaaa%22%2C%22desc%22%3A%22%22%2C%22newcat%22%3A%22nnnnn%22%2C%22newsubcat%22%3A%22sssss%22%2C%22apply_video_origialFlag%22%3A0%2C%22activity%22%3A%22%22%2C%22vid%22%3A%22vvvvv%22%2C%22imgurl%22%3A%22http%3A%2F%2Fpuap.qpic.cn%2Fvpic%2F0%2Fvvvvv_fast_5.jpg%2F0%22%2C%22user_original%22%3A0%2C%22tagsid%22%3A%22%7B%7D%22%2C%22apply_video_originalFlag%22%3A0%2C%22apply_video_vrFlag%22%3A0%2C%22user_vr%22%3A0%2C%22is_commercial%22%3A0%2C%22commodity%22%3A%22%22%2C%22apply_push_flag%22%3A0%2C%22needpub%22%3A1%2C%22uid%22%3A%22cbd0cad84ca17a2c%22%2C%22imgurlsrc%22%3A%22system%22%7D%5D&articles=%5B%7B%22vid%22%3A%22vvvvv%22%2C%22title%22%3A%22ttttt%22%2C%22is_commercial%22%3A0%2C%22user_original%22%3A0%2C%22user_vr%22%3A0%2C%22commodity%22%3A%22%22%2C%22apply_push_flag%22%3A0%2C%22activity%22%3A%22%22%2C%22cover_type%22%3A%22%22%2C%22type%22%3A%2256%22%2C%22content%22%3A%22%3Cp%3E%3Ciframe+allowfullscreen%3D%5C%22%5C%22+f%3D%5C%22no%5C%22+frameborder%3D%5C%220%5C%22+height%3D%5C%22270%5C%22+src%3D%5C%22%2F%2Fv.qq.com%2Fiframe%2Fpreview.html%3Fvid%3Dvvvvv%26amp%3Bwidth%3D480%26amp%3Bheight%3D270%26amp%3Bauto%3D0%5C%22+type%3D%5C%22video%5C%22+width%3D%5C%22480%5C%22%3E%3C%2Fiframe%3E%3C%2Fp%3E%22%2C%22video%22%3A%22%7B%5C%22vid%5C%22%3A%5C%22vvvvv%5C%22%2C%5C%22title%5C%22%3A%5C%22ttttt%5C%22%2C%5C%22type%5C%22%3A%5C%22video%5C%22%2C%5C%22desc%5C%22%3A%5C%22%5C%22%2C%5C%22duration%5C%22%3A%5C%220%3A00%3A00%5C%22%2C%5C%22img%5C%22%3A%7B%7D%7D%22%2C%22needpub%22%3A1%7D%5D'''
    data = data.replace("vvvvv", vid)
    data = data.replace("ttttt", urllib.request.quote(title))
    data = data.replace("aaaaa", encodedtags)
    data = data.replace("nnnnn", urllib.request.quote(newcat))
    data = data.replace("sssss", urllib.request.quote(newsubcat))
    # print()
    # print(aaaa.replace("ttttt", urllib.request.quote(title)))

    # asff = '''videos=[{"title":"，","tags":"宝骏+","desc":"","newcat":"新闻","newsubcat":"","apply_video_origialFlag":0,"activity":"","vid":"w05562chn0y","imgurl":"http://puap.qpic.cn/vpic/0/w05562chn0y_fast_5.jpg/0","user_original":0,"tagsid":"{}","apply_video_originalFlag":0,"apply_video_vrFlag":0,"user_vr":0,"is_commercial":0,"commodity":"","apply_push_flag":0,"needpub":1,"uid":"cbd0cad84ca17a2c","imgurlsrc":"system"}]&articles=[{"vid":"w05562chn0y","title":"国人自制遥控履带车，直接遥控撞五菱宏光","is_commercial":0,"user_original":0,"user_vr":0,"commodity":"","apply_push_flag":0,"activity":"","cover_type":"","type":"56","content":"<p><iframe+allowfullscreen=\"\"+f=\"no\"+frameborder=\"0\"+height=\"270\"+src=\"//v.qq.com/iframe/preview.html?vid=w05562chn0y&amp;width=480&amp;height=270&amp;auto=0\"+type=\"video\"+width=\"480\"></iframe></p>","video":"{\"vid\":\"w05562chn0y\",\"title\":\"国人自制遥控履带车，直接遥控撞五菱宏光\",\"type\":\"video\",\"desc\":\"\",\"duration\":\"0:00:00\",\"img\":{}}","needpub":1}]'''
    logging.info(" data ！" + data)
    # data = urllib.request.quote(data, safe="")
    # logging.info(" data ！" + data)


    # articles[0]["vid"] = vid
    # articles[0]["title"] = file_name
    headers = {
        'Host': 'om.qq.com',
        'User-Agent': useragent,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Content-Length': size,
        # 'Cookie': 'TSID=' + UnFtnReady_TSID,  {"response":{"code":-10403,"msg":"Exception."},"data":[]}
        # 'Cookie': 'pgv_pvi=4977534976; pt2gguin=o0743392069; RK=1XYB4IoBV0; ptcz=c227ecbaa2db628758b51fc0db013f8af3e80ff0fb05bead8fde1689fbe055d8; pgv_pvid=3316797086; o_cookie=743392069; pac_uid=1_743392069; pgv_info=ssid=s4110512380; ts_uid=6537587375; OM_EMAIL='+emailEncoded+'; userid='+userid+'; uin='+uin+'; uid='+uid+'; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; tvfe_boss_uuid=69f7405aadb81e4f; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last=om.qq.com/article/syncWeixin; 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D',
        'Cookie': 'pgv_pvi=' + pgv_pvi + '; pgv_pvid=' + pgv_pvid + '; pgv_info=' + pgv_info + '; ts_uid=' + ts_uid + '; OM_EMAIL=' + email + '; userid=' + userid + '; uin=' + uin + '; fname=' + fname + '; fimgurl=' + fimgurl + '; omtoken=' + omtoken + '; omtoken_expire=' + omtoken_expire + '; rmod=1; TSID=' + UnFtnReady_TSID + '; alertclicked=%7C1%7C; ts_last=' + ts_last + '; ' + a32Key + '=' + a32Value + '',
        # 'Cookie': 'pgv_pvi=' + pgv_pvi + '; pgv_pvid=' + pgv_pvid + '; pgv_info=' + pgv_info + '; ts_uid=' + ts_uid + '; OM_EMAIL=' + email + '; userid=' + userid + '; uin=' + uin + '; fname=' + fname + '; fimgurl=' + fimgurl + '; omtoken=' + omtoken + '; omtoken_expire=' + omtoken_expire + '; rmod=1; TSID=' + UnFtnReady_TSID + '; alertclicked=%7C1%7C; ts_last=' + ts_last + '; ' + a32Key + '=' + a32Value + '',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }
        # Cookie: pgv_pvi=4977534976; pt2gguin=o0743392069; RK=1XYB4IoBV0; ptcz=c227ecbaa2db628758b51fc0db013f8af3e80ff0fb05bead8fde1689fbe055d8; pgv_pvid=3316797086; o_cookie=743392069; pac_uid=1_743392069; pgv_info=ssid=s4110512380; ts_uid=6537587375; OM_EMAIL=xdlc79@163.com; userid=6366243; uin=o0743392069; uid=753181314; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; TSID=75hqs61fipn55l50k0trq3luk1; omtoken=548c8ad189; omtoken_expire=1518071140; rmod=1; ts_last=om.qq.com/article/syncWeixin; tvfe_boss_uuid=69f7405aadb81e4f; alertclicked=%7C1%7C; 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D

    # logging.info(articles)
    # logging.info(videos)

    # 暂时就不要 batchPublish
    # data = {"articles": articles, "videos": videos}
    # logging.info("")
    # logging.info(data)
    r = s.post('https://om.qq.com/article/batchPublish?relogin=1', data=data, headers=headers)
    ## logging.info(r.status_code)
    logging.info(r.text)
    # logging.info(r.cookies)
    time.sleep(1)
    jsonRst = r.json()
    code = jsonRst["response"]["code"]
    msg = jsonRst["response"]["msg"]
    if code != 0:
        logging.error("发布失败！" + file_name)
        return 6,vid
    else:
        logging.info("发布成功！" + file_name)
        try:
            aid = jsonRst["data"][vid]["aid"]
            # logging.info("发布成功！" + aid)
            # return 100,vid,aid
            return aid, vid
        except Exception as e:
            logging.info("发布失败！" + str(e))

    time.sleep(1)

    updatestr = {
        "vid": vid,
        "title": title,
        "newcat": newcat,
        "newsubcat": newsubcat,
        "tags": tags, # fun+cute+exciting
        "tagsid": {},
        "desc":"",
        "apply_video_originalFlag":0,
        "imgurl":""
    }

    headers = {
        'Host': 'om.qq.com',
        'User-Agent': useragent,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Content-Length': size,
        # 'Cookie': 'TSID=' + UnFtnReady_TSID,  {"response":{"code":-10403,"msg":"Exception."},"data":[]}
        # 'Cookie': 'pgv_pvi=4977534976; pt2gguin=o0743392069; RK=1XYB4IoBV0; ptcz=c227ecbaa2db628758b51fc0db013f8af3e80ff0fb05bead8fde1689fbe055d8; pgv_pvid=3316797086; o_cookie=743392069; pac_uid=1_743392069; pgv_info=ssid=s4110512380; ts_uid=6537587375; OM_EMAIL='+emailEncoded+'; userid='+userid+'; uin='+uin+'; uid='+uid+'; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; tvfe_boss_uuid=69f7405aadb81e4f; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last=om.qq.com/article/syncWeixin; 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D',
        'Cookie': 'pgv_pvi=' + pgv_pvi + '; pgv_pvid=' + pgv_pvid + '; pgv_info=' + pgv_info + '; ts_uid=' + ts_uid + '; OM_EMAIL=' + email + '; userid=' + userid + '; uin=' + uin + '; fname=' + fname + '; fimgurl=' + fimgurl + '; omtoken=' + omtoken + '; omtoken_expire=' + omtoken_expire + '; rmod=1; TSID=' + UnFtnReady_TSID + '; alertclicked=%7C1%7C; ts_last=' + ts_last + '; ' + a32Key + '=' + a32Value + '',
        # 'Cookie': 'pgv_pvi=' + pgv_pvi + '; pgv_pvid=' + pgv_pvid + '; pgv_info=' + pgv_info + '; ts_uid=' + ts_uid + '; OM_EMAIL=' + email + '; userid=' + userid + '; uin=' + uin + '; fname=' + fname + '; fimgurl=' + fimgurl + '; omtoken=' + omtoken + '; omtoken_expire=' + omtoken_expire + '; rmod=1; TSID=' + UnFtnReady_TSID + '; alertclicked=%7C1%7C; ts_last=' + ts_last + '; ' + a32Key + '=' + a32Value + '',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }
        # Cookie: pgv_pvi=4977534976; pt2gguin=o0743392069; RK=1XYB4IoBV0; ptcz=c227ecbaa2db628758b51fc0db013f8af3e80ff0fb05bead8fde1689fbe055d8; pgv_pvid=3316797086; o_cookie=743392069; pac_uid=1_743392069; pgv_info=ssid=s4110512380; ts_uid=6537587375; OM_EMAIL=xdlc79@163.com; userid=6366243; uin=o0743392069; uid=753181314; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; TSID=75hqs61fipn55l50k0trq3luk1; omtoken=548c8ad189; omtoken_expire=1518071140; rmod=1; ts_last=om.qq.com/article/syncWeixin; tvfe_boss_uuid=69f7405aadb81e4f; alertclicked=%7C1%7C; 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D

    logging.info("")
    r = s.post('https://om.qq.com/VideoManager/UpdateVideoInfo?relogin=1', data=updatestr, headers=headers)
    ## logging.info(r.status_code)
    logging.info(r.text)
    ## logging.info(r.cookies)
    time.sleep(1)

    jsonRst = r.json()
    code = jsonRst["response"]["code"]
    msg = jsonRst["response"]["msg"]
    if code != 0:
        logging.error("发布失败！" + msg)
        return 7,vid
    else:
        logging.info("发布成功！" + msg)
        return 101,vid


