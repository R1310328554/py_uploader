# -*- coding:utf-8 -*-

import json
import logging
import os
import time
import urllib.request

import base
from xmlUtil import read_xml_from_txt

############################## 获取登录信息 ##############################
# open_uid = "6366243"

alertclicked = "%7C1%7C" #coo.get("alertclicked")
a32Key = "9e67236d07bdc7152e6e2b42b7f00f43"  #　来源于  signin


# def upload(r, userid, fimgurl, fname, cbvp ,omtoken,omtoken_expire,randomkey,TSID,a32Key,a32Value):
def upload(email, sess, userid, open_token, video_file, newcat, newsubcat, tags):
    local_file = video_file.name
    ind = local_file.rfind("\\", 0)
    file_name = local_file[ind+1:]
    ind2 = file_name.rfind(".", 0) # 如果没有后缀。。
    file_suffix = file_name[ind2+1:]
    file_name_no_suffix = file_name[0:ind2]
    file_name_no_suffix_urlencoded = urllib.request.quote(file_name_no_suffix)
    size = str(os.path.getsize(local_file))

    logging.info("=========================== 准备上传文件:%s, userid:%s" %(file_name, userid))
    open_uid = userid
    mediaid = open_uid

    uin="o0514870968"

    fid = ""
    vid = ""
    # email = "xdlc79@163.com"
    # emailEncoded = "xdlc79&40163.com"
    # email = "xdlc79&40163.com"
    # email = "fi6956@163.com"
    # email = "upqv97%40163.com"
    #   upqv97@163.com----qqq123qqq

    pgv_pvid = "623613877"

    r = sess.get("https://pingfore.qq.com/pingd?dm=om.qq.com&url=/userAuth/index&rdm=om.qq.com&rurl=/data/index&rarg=-&pvid=" + pgv_pvid + "&scr=1467x825&scl=24-bit&lang=zh-cn&java=0&pf=Win64&tz=-8&flash=-&ct=-&vs=tcss.3.1.5&ext=tm%3D1&hurlcn=&rand=88746&reserved1=-1&tt=")
    r = sess.get("https://pingtas.qq.com/webview/pingd?dm=taclick&pvi=714581518355265759&si=s902171518550888644&url=video_publish_video_publish_uploadvideo&arg=&ty=0&rdm=om.qq.com&rurl=/article/videomanage&rarg=&adt=&r2=500549930&r5=&scr=1366x768&scl=24-bit&lg=zh-cn&tz=-8&ext=version=2.0.6&random=1518609693391")
    r = sess.get("https://pingfore.qq.com/pingd?dm=om.qq.com&url=/userAuth/index&rdm=om.qq.com&rurl=/data/index&rarg=-&pvid=" + pgv_pvid + "&scr=1467x825&scl=24-bit&lang=zh-cn&java=0&pf=Win64&tz=-8&flash=-&ct=-&vs=tcss.3.1.5&ext=tm%3D1&hurlcn=&rand=88746&reserved1=-1&tt=")

    relogin = "?relogin=1'"
    relogin2 = "&relogin=1"

    starttime = time.time()
    r = sess.get('https://om.qq.com/VideoManager/VideoCatagory' + relogin)
    # logging.info(r)
    # logging.info(r.text)
    TSID = str(r.cookies.get("TSID"))

    r = sess.get('https://om.qq.com/VideoManager/GetUserTags?title=' + file_name_no_suffix_urlencoded + relogin2)


    video_file.seek(0)
    videa_md5 = base.getFileMd5ByName1(video_file)
    video_file.seek(0)
    videa_sha1 = base.getFileShaByName1(video_file)
    # postdata = "qzreferrer=https%3A%2F%2Fom.qq.com%2Farticle%2FarticlePublish%23%2F%21%2Fview%3Aarticle%3FtypeName%3Dmultivideos&vid=&bid=open_omg_video&type=24&tags=&cat=&act=&title=&folder=&orifname="+file_name+"&size="+size+"&uptype=3&key=&open_uid="+open_uid+"&open_token="+open_token+"&uin=0&encuin=&g_tk=&otype=json"
    qzreferrer = "https://om.qq.com/article/articlePublish#/!/view:article?typeName=multivideos"
    postdata = {
        "qzreferrer": urllib.request.quote(qzreferrer),
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
        "orifname": file_name_no_suffix+".mp4",
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

    headers = {
        # "cookie": "pgv_pvi=9404854272; RK=qRqAq7SBev; __guid=212959114.289882160309224300.1522849295918.1545; ts_refer=www.so.com/s; ptcz=ebae3b5bd8c50de9bcd4abf034a825265e2ae6617e726b57644704c31623c9d7; pt2gguin=o1310328554; OM_EMAIL=abbp62@163.com; fname=%E6%97%85%E4%BA%BA%E4%B8%8E%E9%A3%8E%E4%BF%97; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F317718547_200200%2F0; userid=5171401; omtoken=2ae8b7bc10; omtoken_expire=1529141333; rmod=1; tvfe_boss_uuid=41627d9419d7226c; mobileUV=1_16406e60af9_56c10; o_cookie=1310328554; alertclicked=%7C1%7C; pgv_info=ssid=s7088195291; pgv_pvid=8020344988; ts_uid=5157774494; monitor_count=30; TSID=5d9romhfh071435ufa6ig18v45; 9e67236d07bdc7152e6e2b42b7f00f43=7bffd563ac2c576cecaf49a5e59684cd2bce7998a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25225171401%2522%253Bi%253A1%253Bs%253A14%253A%2522abbp62%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A14%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522abbp62%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A4%253A%2522wxid%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A54%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F317718547_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E6%2597%2585%25E4%25BA%25BA%25E4%25B8%258E%25E9%25A3%258E%25E4%25BF%2597%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25225171401%2522%253B%257D%257D",
        # "referer":"https://om.qq.com/article/articlePublish",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.8",
        "cache-control": "max-age=0",
        # "content-length": size,
        "content-type": "application/x-www-form-urlencoded",
        # "cookie": "pgv_pvi=9404854272; RK=qRqAq7SBev; __guid=212959114.289882160309224300.1522849295918.1545; ts_refer=www.so.com/s; ptcz=ebae3b5bd8c50de9bcd4abf034a825265e2ae6617e726b57644704c31623c9d7; pt2gguin=o1310328554; OM_EMAIL=abbp62@163.com; fname=%E6%97%85%E4%BA%BA%E4%B8%8E%E9%A3%8E%E4%BF%97; fimgurl=http%3A%2F%2Finews.gtimg.com%2Fnewsapp_ls%2F0%2F317718547_200200%2F0; userid=5171401; omtoken=2ae8b7bc10; omtoken_expire=1529141333; rmod=1; tvfe_boss_uuid=41627d9419d7226c; mobileUV=1_16406e60af9_56c10; o_cookie=1310328554; alertclicked=%7C1%7C; pgv_info=ssid=s7088195291; pgv_pvid=8020344988; ts_uid=5157774494; monitor_count=30; TSID=5d9romhfh071435ufa6ig18v45; 9e67236d07bdc7152e6e2b42b7f00f43=7bffd563ac2c576cecaf49a5e59684cd2bce7998a%253A4%253A%257Bi%253A0%253Bs%253A7%253A%25225171401%2522%253Bi%253A1%253Bs%253A14%253A%2522abbp62%2540163.com%2522%253Bi%253A2%253Bi%253A43200%253Bi%253A3%253Ba%253A14%253A%257Bs%253A6%253A%2522status%2522%253Bi%253A2%253Bs%253A5%253A%2522email%2522%253Bs%253A14%253A%2522abbp62%2540163.com%2522%253Bs%253A9%253A%2522logintype%2522%253Bi%253A1%253Bs%253A3%253A%2522uin%2522%253BN%253Bs%253A5%253A%2522phone%2522%253BN%253Bs%253A4%253A%2522wxid%2522%253BN%253Bs%253A6%253A%2522imgurl%2522%253Bs%253A54%253A%2522http%253A%252F%252Finews.gtimg.com%252Fnewsapp_ls%252F0%252F317718547_200200%252F0%2522%253Bs%253A4%253A%2522name%2522%253Bs%253A15%253A%2522%25E6%2597%2585%25E4%25BA%25BA%25E4%25B8%258E%25E9%25A3%258E%25E4%25BF%2597%2522%253Bs%253A10%253A%2522isVerified%2522%253Bb%253A1%253Bs%253A10%253A%2522isRejected%2522%253Bb%253A0%253Bs%253A9%253A%2522agreeAcpt%2522%253Bb%253A0%253Bs%253A6%253A%2522pwdChg%2522%253Bb%253A0%253Bs%253A9%253A%2522avatarChg%2522%253Bb%253A0%253Bs%253A2%253A%2522id%2522%253Bs%253A7%253A%25225171401%2522%253B%257D%257D",
        "origin": "https://om.qq.com",
        "referer": "https://om.qq.com/article/articlePublish",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }

    logging.info("开始上传 ... ")
    "https://om.qq.com/VideoUpload/FtnReady?g_tk="
    # r = sess.post('https://om.qq.com/VideoUpload/UnFtnReady?g_tk=', data=postdata, headers=headers)
    r = sess.post('https://om.qq.com/VideoUpload/FtnReady?g_tk=', data=postdata, headers=headers)
    # logging.info(r.status_code)
    # logging.info(r.text)
    ## logging.info(r.cookies)

    indexStr = "frameElement.callback("
    ind1 = r.text.find(indexStr)
    ind2 = r.text.find("});")
    if ind2 > ind1 > 0:
        callbackJsonStr = r.text[ind1 + len(indexStr): ind2 + 1]
        callbackJson = json.loads(callbackJsonStr)
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
    else:
        logging.error(" 上传失败 UnFtnReady ==>  "  + r.text)
        exit(-1)
        # return 1, -1
    ### r.close()

    video_file.seek(0)
    length = 512 * 1024
    allMd5 = base.getFileMd5List(video_file, length)
    video_file.seek(0)
    for sectionMd5 in allMd5:
        upUrl = "https://sh.ugc.ftn.qq.com/ftn_handler?bmd5="+sectionMd5
        r = sess.options(upUrl)
        if r.status_code == 200:
            hh = r.headers["X-NWS-LOG-UUID"]
            print("X-NWS-LOG-UUID", hh)
            buffer = video_file.read(length)
            logging.info("上传中  %s " % len(buffer))
            r = sess.post(upUrl, data=buffer)
            content = r.content
            print("content", content)
            print("r text  ", r.text)
            if r.status_code == 200:
                hh = r.headers["X-NWS-LOG-UUID"]
                print("X-NWS-LOG-UUID", hh)

                hh = r.headers["Content-Range"]
                print("Content-Range", hh)

    r = sess.get('https://om.qq.com/VideoManager/GetUserTags?title=' + file_name_no_suffix + relogin2)
    # logging.info(r.text)
    jsonRst = r.json()
    recommend_tags = jsonRst["data"]["recommend_tags"]

    if len(recommend_tags) >= 5:
        tagsList = recommend_tags[0:5]
    else:
        tagsList = tags.split(",")
    encodedtags = "+".join(list(map(lambda x:urllib.request.quote(x.strip(" ")), tagsList)))

    time.sleep(1)
    uploadurl = 'https://uu.video.qq.com/v1/openvupvideo?g_tk='
    r = sess.options(uploadurl)

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

    bound = "4021056925725";
    logging.info("上传中 ... " + file_name)

    # headers['content-type'] = 'charset=iso8859-1'
    r = sess.post(uploadurl, data=postdata)
    # eee = r.encoding

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

    finishedtime = time.time()

    timeconsume = int((finishedtime - starttime) * 1000)
    logging.info("上传耗时(ms) ： %i " % timeconsume)

    time.sleep(1)
    postdata = {
        "desc": "视频上传",
        "errorcode":0,
        "errormsg":"上传成功",
        "interface":"upload",
        "machineinfo":{"system":"win7","browser":"firefox","navigar": base.useragent,"flashver":27,"cookie":"开启","javascript":"开启","localstorage":"开启"},
        "params":{"mediaid": mediaid},
        "reponse":"{}",
        "timeconsume":timeconsume,
        "vid":vid
    }
    headers = {
        'Host': 'om.qq.com',
        'User-Agent': base.useragent,
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Content-Length': '556',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }

    logging.info("")
    logging.info("确认上传 ... ")
    r = sess.post('https://om.qq.com/videoUpload/Finished' + relogin, data=postdata, headers=headers)

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

    cnt = 0
    while cnt < 100:
        getRet = "https://puap.qpic.cn/vpic/0/d0691y3s6wv_fast_5.jpg/0?t=%s"+ cnt
        sess.get(getRet)
        if r.status_code == 200:
            chid = r.textr.headers["chid"]
            fid = r.textr.headers["fid"]
            server = r.textr.headers["fid"]
            size = r.textr.headers["fid"]

    #  发布文件
    title = file_name_no_suffix
    desc = ""
    fileType = "video"
    duration = "0:00:00 "
    headers = {
        'Host': 'om.qq.com',
        'User-Agent': base.useragent,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }
    r = sess.get('https://om.qq.com/videoManager/checkVideoParam?title=' + title + '&tags=' + tags + '&desc=' + desc + '&relogin=1', headers=headers)
    ## logging.info(r.status_code)
    logging.info(r.text)
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
    r = sess.post(changeParamUrl)
    ## logging.info(r.status_code)
    logging.info(r.text)
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
    loop = 0
    while(loop < 20):
        time.sleep(3)
        r = sess.head("https://puap.qpic.cn/vpic/0/" + vid + "_fast_5.jpg/0?t=" + str(loop))
        loop = loop + 1
        status_code = r.status_code
        # print(status_code)
        if status_code == 200:
            logging.info(" _fast_5.jpg 生成ok ！" + str(loop))
            break

    if loop >= 20:
        return 5,vid

    # data = 'videos=[{"title":"'+ title +'","tags":"'+ tags +'","desc":"","newcat":"'+ newcat +'","newsubcat":"'+ newsubcat +'","apply_video_origialFlag":0,"activity":"","vid":"'+ vid +'","imgurl":"http://puap.qpic.cn/vpic/0/'+ vid +'_fast_5.jpg/0","user_original":0,"tagsid":"{}","apply_video_originalFlag":0,"apply_video_vrFlag":0,"user_vr":0,"is_commercial":0,"commodity":"","apply_push_flag":0,"needpub":1,"uid":"cbd0cad84ca17a2c","imgurlsrc":"system"}]&articles=[{"vid":"'+ vid +'","title":"'+ title +'","is_commercial":0,"user_original":0,"user_vr":0,"commodity":"","apply_push_flag":0,"activity":"","cover_type":"","type":"56","content":"<p><iframe+allowfullscreen=\"\"+f=\"no\"+frameborder=\"0\"+height=\"270\"+src=\"//v.qq.com/iframe/preview.html?vid='+ vid +'&amp;width=480&amp;height=270&amp;auto=0\"+type=\"video\"+width=\"480\"></iframe></p>","video":"{\"vid\":\"'+ vid +'\",\"title\":\"'+ title +'\",\"type\":\"video\",\"desc\":\"\",\"duration\":\"0:00:00\",\"img\":{}}","needpub":1}]'
    data = '''videos=%5B%7B%22title%22%3A%22ttttt%22%2C%22tags%22%3A%22aaaaa%22%2C%22desc%22%3A%22%22%2C%22newcat%22%3A%22nnnnn%22%2C%22newsubcat%22%3A%22sssss%22%2C%22apply_video_origialFlag%22%3A0%2C%22activity%22%3A%22%22%2C%22vid%22%3A%22vvvvv%22%2C%22imgurl%22%3A%22http%3A%2F%2Fpuap.qpic.cn%2Fvpic%2F0%2Fvvvvv_fast_5.jpg%2F0%22%2C%22user_original%22%3A0%2C%22tagsid%22%3A%22%7B%7D%22%2C%22apply_video_originalFlag%22%3A0%2C%22apply_video_vrFlag%22%3A0%2C%22user_vr%22%3A0%2C%22is_commercial%22%3A0%2C%22commodity%22%3A%22%22%2C%22apply_push_flag%22%3A0%2C%22needpub%22%3A1%2C%22uid%22%3A%22cbd0cad84ca17a2c%22%2C%22imgurlsrc%22%3A%22system%22%7D%5D&articles=%5B%7B%22vid%22%3A%22vvvvv%22%2C%22title%22%3A%22ttttt%22%2C%22is_commercial%22%3A0%2C%22user_original%22%3A0%2C%22user_vr%22%3A0%2C%22commodity%22%3A%22%22%2C%22apply_push_flag%22%3A0%2C%22activity%22%3A%22%22%2C%22cover_type%22%3A%22%22%2C%22type%22%3A%2256%22%2C%22content%22%3A%22%3Cp%3E%3Ciframe+allowfullscreen%3D%5C%22%5C%22+f%3D%5C%22no%5C%22+frameborder%3D%5C%220%5C%22+height%3D%5C%22270%5C%22+src%3D%5C%22%2F%2Fv.qq.com%2Fiframe%2Fpreview.html%3Fvid%3Dvvvvv%26amp%3Bwidth%3D480%26amp%3Bheight%3D270%26amp%3Bauto%3D0%5C%22+type%3D%5C%22video%5C%22+width%3D%5C%22480%5C%22%3E%3C%2Fiframe%3E%3C%2Fp%3E%22%2C%22video%22%3A%22%7B%5C%22vid%5C%22%3A%5C%22vvvvv%5C%22%2C%5C%22title%5C%22%3A%5C%22ttttt%5C%22%2C%5C%22type%5C%22%3A%5C%22video%5C%22%2C%5C%22desc%5C%22%3A%5C%22%5C%22%2C%5C%22duration%5C%22%3A%5C%220%3A00%3A00%5C%22%2C%5C%22img%5C%22%3A%7B%7D%7D%22%2C%22needpub%22%3A1%7D%5D'''
    data = data.replace("vvvvv", vid)
    data = data.replace("ttttt", urllib.request.quote(title))
    data = data.replace("aaaaa", encodedtags)
    data = data.replace("nnnnn", urllib.request.quote(newcat))
    data = data.replace("sssss", urllib.request.quote(newsubcat))
    logging.info(" data ！" + data)

    headers = {
        'Host': 'om.qq.com',
        'User-Agent': base.useragent,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }

    r = sess.post('https://om.qq.com/article/batchPublish?relogin=1', data=data, headers=headers)
    logging.info(r.text)
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
        'User-Agent': base.useragent,
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://om.qq.com/article/articlePublish',
    }
    logging.info("")

    info_relogin_ = 'https://om.qq.com/VideoManager/UpdateVideoInfo?relogin=1'
    info_relogin_ = "Request URL:https://om.qq.com/article/getWhiteListOfWordsInTitle?relogin=1"

    r = sess.post('%s' % info_relogin_, data=updatestr, headers=headers)
    logging.info(r.text)
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
