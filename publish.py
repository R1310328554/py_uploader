# -*- coding:utf-8 -*-

import logging
import os

import requests
import hashlib
import json

import time
import xlrd
import xlwt

from ExcelUtil import excel_table_byname


# open_uid = "6366243"
# userid = "6366243"
# uid = "82589a9b22dd3256"
# uin = "o0743392069"
# open_token = "feb0596663"
# omtoken = "feb0596663"
# omtoken = "c5569aeb61"
# omtoken_expire = "1518196588"
# origframe = "delete.avi"
# TSID = "vb41d3d91l334h56kqo18p26q1" # piskuncs6vcic0kied13u0rii1
# size = 222
# fid = "180209olm2y"
# vid = "h0548n9cfsz"
# upload_file = "C:\\Windows\\winsxs\\amd64_microsoft-windows-tabletpc-inputpanel_31bf3856ad364e35_6.1.7601.17514_none_6fb51b358e21d75f\\delete.avi"
# upload_file = "C:\\Program Files\\Common Files\\Microsoft Shared\\ink\\FlickAnimation.avi"
# # upload_file = "C:\\Windows\\winsxs\\amd64_microsoft-windows-tabletpc-inputpanel_31bf3856ad364e35_6.1.7601.23187_none_6ff5d25ca775c844\\correct.avi"
# ind = upload_file.rfind("\\", 0)
# file_name = upload_file[ind+1:]
# size = str(os.path.getsize(upload_file))
# tick = str(int(time.time()*1000))
# email = "xdlc79@163.com"
# email = "xdlc79@163.com"
# emailEncoded = "xdlc79&40163.com"

# _qpsvr_localtk	0.21071425067725524
# eas_sid	r1M5f0w5Y9N9f526Z415L7N597
# mobileUV	1_15a13bae06c_24dd6
# o_cookie	1310328554
# pac_uid	1_1310328554
# pgv_info	ssid=s3368838360
# pgv_pvi	9051836416
# pgv_pvid	623613877
# pgv_si	s6626417664
# pt2gguin	o1310328554
# ptcz	f6a7f98cc4db828bf43c8d66135b4275959740a26deb6df9e661ed54ecfc9af0
# ptisp	ctc
# qm_authimgs_id	3
# qm_verifyimagesession	h01eb5cfafc3caa8a6c93c0dc60ff7155c567ac7ae8543199571d2aad15efea57ca3542321626d4a513
# RK	TjtTSvs+f6
# tvfe_boss_uuid	c4bb75a40e8251b5
# uin	o0514870968

uin = "o0514870968"
ts_uid = "4442968678"
uid = "640f64f657fa1fb3"  # xxx
pgv_pvi = "9051836416"  # 本地存储 ， 这个参数不是每次都会附带 39104 1518230262564
pgv_si = "s6626417664"  # 会话存储 ， 这个参数不是每次都会附带 s6432 1518230262564
pgv_pvid = "623613877"
# pgv_pvid = "4618129525"
pgv_info = "ssid=s3368838360"
pt2gguin = "o1310328554"
o_cookie = "1310328554"
ts_last = "om.qq.com/article/articleManage"
sid = "CG3h0aZKftVIIy_qVC1uR1-DjsGllRFDMW8_6-Hoto2T1fkWozweXm3toGk9ypuq"
csrfToken = "omfPyrf_LBmM3bpMrsYmPYfk"
uin = "0"
ptcz = "f6a7f98cc4db828bf43c8d66135b4275959740a26deb6df9e661ed54ecfc9af0"
RK = "TjtTSvs+f6"
pac_uaaidaa = ""
pac_uid = "1_1310328554"
tvfe_boss_uuid = "c4bb75a40e8251b5"
relogin = "?relogin=1'"
relogin2 = "&relogin=1'"

userid = "6366243"
omtoken = "d462dc7df7"
omtoken_expire = "1518423045"
a32Key = "9e67236d07bdc7152e6e2b42b7f00f43"  #　来源于  signin
a32Value =  "46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D"
file_name = "Megamind_bugy.avi"
fname="%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85"
fimgurl="http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0"
email = 'xdlc79@163.com'
email = "upqv97@163.com"
emailEnc = "upqv97%40163.com"


# uid = "8bbd579f09e54d1d" # uid 不是 userid !
def publish(s, vid, newcat, newsubcat,desc, tags, duration, title, fileType="video", uid= "8bbd579f09e54d1d"):

    # articles[0]["vid"] = vid
    # articles[0]["title"] = file_name
    headers = {
        'Host': 'om.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
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
    logging.info(r.status_code)
    logging.info(r.text)
    logging.info(r.cookies)

    jsonRst = r.json() # 验证通过， 正常返回是： {"response":{"code":0,"msg":"suc"},"data":null}
    code = jsonRst["response"]["code"]
    msg = jsonRst["response"]["msg"] # 验证成功是 succ
    # new_TSID = ""
    if code != 0:
        logging.info("验证失败！" + msg)
        return "验证失败 ： " + msg
    else:
        logging.info("验证成功 ！" + msg)
        UnFtnReady_TSID = str(r.cookies.get("TSID"))

    articles =	[{"vid":vid,"title":title,"is_commercial":0,"user_original":0,"user_vr":0,"commodity":"","apply_push_flag":0,"activity":"","cover_type":"","type":"56","content":"<p><iframe+allowfullscreen=\"\"+f=\"no\"+frameborder=\"0\"+height=\"270\"+src=\"//v.qq.com/iframe/preview.html?vid="+vid+"&amp;width=480&amp;height=270&amp;auto=0\"+type=\"video\"+width=\"480\"></iframe></p>","video":"{\"vid\":\""+vid+"\",\"title\":\""+title+"\",\"type\":\""+fileType+"\",\"desc\":\""+desc+"\",\"duration\":\""+duration+"\",\"img\":{}}","needpub":1}]
    videos =	[{"title":title,"tags":tags,"desc":desc,"newcat":newcat,"newsubcat":newsubcat,"apply_video_origialFlag":0,"activity":"","vid":vid,"imgurl":"http://puap.qpic.cn/vpic/0/"+vid+"_fast_5.jpg/0","user_original":0,"tagsid":"{}","apply_video_originalFlag":0,"apply_video_vrFlag":0,"user_vr":0,"is_commercial":0,"commodity":"","apply_push_flag":0,"needpub":1,"uid":uid,"imgurlsrc":"system"}]

    # articles[0]["vid"] = vid
    # articles[0]["title"] = file_name
    headers = {
        'Host': 'om.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
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

    logging.info(articles)
    logging.info(videos)
    data = {"articles": articles, "videos": videos}
    logging.info("")
    logging.info(data)
    r = s.post('https://om.qq.com/article/batchPublish?relogin=1', data=data, headers=headers)
    logging.info(r.status_code)
    logging.info(r.text)
    logging.info(r.cookies)

    jsonRst = r.json()
    code = jsonRst["response"]["code"]
    msg = jsonRst["response"]["msg"]
    if code != 0:
        logging.info("发布失败！" + msg)
        return msg
    else:
        return jsonRst

def updateVideoInfo(sess, vid, category, subcategory, desc, tags, duration, title):

    updatestr = {
        "vid": vid,
        "title": title+" 2018平台首发",
        "newcat": category,
        "newsubcat": subcategory,
        "tags": tags+"+aaa+bbbc+ccddd",
        "tagsid": "{}",
        "desc":desc,
        "apply_video_originalFlag":0,
        "imgurl":""
    }

    TSID = "au1vvbun3fdps2c1am0djld3l3"
    headers = {
        'Host': 'om.qq.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        # 'Content-Length': size,
        # 'Cookie': 'TSID=' + UnFtnReady_TSID,  {"response":{"code":-10403,"msg":"Exception."},"data":[]}
        # 'Cookie': 'pgv_pvi=4977534976; pt2gguin=o0743392069; RK=1XYB4IoBV0; ptcz=c227ecbaa2db628758b51fc0db013f8af3e80ff0fb05bead8fde1689fbe055d8; pgv_pvid=3316797086; o_cookie=743392069; pac_uid=1_743392069; pgv_info=ssid=s4110512380; ts_uid=6537587375; OM_EMAIL='+emailEncoded+'; userid='+userid+'; uin='+uin+'; uid='+uid+'; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; omtoken='+omtoken+'; omtoken_expire='+omtoken_expire+'; rmod=1; tvfe_boss_uuid=69f7405aadb81e4f; TSID='+TSID+'; alertclicked=%7C1%7C; ts_last=om.qq.com/article/syncWeixin; 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D',
        # 'Cookie': 'pgv_pvi=' + pgv_pvi + '; pgv_pvid=' + pgv_pvid + '; pgv_info=' + pgv_info + '; ts_uid=' + ts_uid + '; OM_EMAIL=' + email + '; userid=' + userid + '; uin=' + uin + '; fname=' + fname + '; fimgurl=' + fimgurl + '; omtoken=' + omtoken + '; omtoken_expire=' + omtoken_expire + '; rmod=1; TSID=' + UnFtnReady_TSID + '; alertclicked=%7C1%7C; ts_last=' + ts_last + '; ' + a32Key + '=' + a32Value + '',
        'Cookie': 'pgv_pvi=' + pgv_pvi + '; pgv_pvid=' + pgv_pvid + '; pgv_info=' + pgv_info + '; ts_uid=' + ts_uid + '; OM_EMAIL=' + email + '; userid=' + userid + '; uin=' + uin + '; fname=' + fname + '; fimgurl=' + fimgurl + '; omtoken=' + omtoken + '; omtoken_expire=' + omtoken_expire + '; rmod=1; TSID=' + TSID + '; alertclicked=%7C1%7C; ts_last=' + ts_last + '; ' + a32Key + '=' + a32Value + '',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }
        # Cookie: pgv_pvi=4977534976; pt2gguin=o0743392069; RK=1XYB4IoBV0; ptcz=c227ecbaa2db628758b51fc0db013f8af3e80ff0fb05bead8fde1689fbe055d8; pgv_pvid=3316797086; o_cookie=743392069; pac_uid=1_743392069; pgv_info=ssid=s4110512380; ts_uid=6537587375; OM_EMAIL=xdlc79@163.com; userid=6366243; uin=o0743392069; uid=753181314; fname=%E5%A5%87%E8%B6%A3%E6%97%85%E8%A1%8C%E8%80%85; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F2634227125_200200%2F0; TSID=75hqs61fipn55l50k0trq3luk1; omtoken=548c8ad189; omtoken_expire=1518071140; rmod=1; ts_last=om.qq.com/article/syncWeixin; tvfe_boss_uuid=69f7405aadb81e4f; alertclicked=%7C1%7C; 9e67236d07bdc7152e6e2b42b7f00f43=46ceb65146b9fa625672dc43e9d123652a0505c7a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25226366243%2522%253Bi%253A1%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A13%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522xdlc79%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A55%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F2634227125_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E5%25A5%2587%25E8%25B6%25A3%25E6%2597%2585%25E8%25A1%258C%25E8%2580%2585%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25226366243%2522%253B%257D%257D
    # ?relogin = 1
    logging.info("")
    r = sess.post('https://om.qq.com/VideoManager/UpdateVideoInfo', data=updatestr, headers=headers)
    logging.info(r.status_code)
    logging.info(r.text)
    logging.info(r.cookies)

    jsonRst = r.json()
    code = jsonRst["response"]["code"]
    msg = jsonRst["response"]["msg"]
    if code != 0:
        logging.info("发布失败！" + msg)
        return msg
    else:
        logging.info("发布成功！" + msg)
        return jsonRst
