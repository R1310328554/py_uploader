# -*- coding:utf-8 -*-

import json
import os
import shutil
import urllib.request

import time
import configparser

import sys

import ExcelUtil
import base
import xmlUtil
import login
import requests
import upload
import publish
import logging


# videoBase = "C:\\Windows\\winsxs\\"
# videoBase = "C:\\Windows\\winsxs\\amd64_microsoft-windows-tabletpc-inputpanel_31bf3856ad364e35_6.1.7601.18984_none_6f695c918e5aa933\\"
# videoBase = "D:\\Program Files (x86)\\Android\\android-sdk\\docs\\training\\animation\\"
# videoBase = "D:\\soft\\cv\\opencv\\sources\\samples\\data\\"
# uploadedBase = "D:\\zzxc\\"
# videoBase = "D:\\BaiduYunDownload\\bd\\testtt\\"

# suffixes = [".avi",".mp4",".rmvb",".wqv",]
# excludeStarts = [] #"aaMegamind","tree",]
# suffixes = [".avi"]

videoBase, excel_file, uploadedBase, publish_interval, location_cookies, location_uploads, suffixes, includeStarts, excludeStarts, single_max_try = "","","","","","","","","","",

def init():
    global videoBase, excel_file, uploadedBase, failedBase, publish_interval, location_cookies, location_uploads, suffixes, includeStarts, excludeStarts, single_max_try
    config = configparser.ConfigParser()
    with open("om.cfg", "r+") as cfgfile:
        config.read_file(cfgfile)
        logging_level = config.get("OM_BASE", "logging.level")
        logging_file = config.get("OM_BASE", "logging.file")
        print("日志文件：", logging_file)
        # 在logging.basciConfig中指定文件和写入方式

        logger = logging.getLogger()  # 创建默认logger
        # 创建handler
        hterm = logging.StreamHandler()  # 输出到终端
        hfile = logging.FileHandler(logging_file, mode="a")  # 输出到文件
        # 定义日志格式
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        # 将日志格式应用到handler
        hterm.setFormatter(formatter)
        # hterm.setLevel(logging.DEBUG)
        hfile.setFormatter(formatter)
        # hfile.setLevel(logging.DEBUG)
        # 给logger添加handler
        logger.addHandler(hterm)
        logger.addHandler(hfile)
        logger.setLevel(logging_level)
        # logging.basicConfig(level=logging_level,
        #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        #                     datefmt='%a, %d %b %Y %H:%M:%S', filename=logging_file, filemode='a')

        videoBase = config.get("OM_BASE", "videoBase")
        excel_file = config.get("OM_BASE", "excel.file")
        uploadedBase = config.get("OM_BASE", "uploadedBase")
        try:
            publish_interval = int(config.get("OM_BASE", "publish.interval"))
        except Exception as e:
            publish_interval = 3
        try:
            location_cookies = int(config.get("OM_BASE", "location.cookies"))
        except Exception as e:
            location_cookies = "cookies"
        try:
            location_uploads = int(config.get("OM_BASE", "location.uploads"))
        except Exception as e:
            location_uploads = "uploads"
			
        try:
            failedBase = int(config.get("OM_BASE", "failed.base"))
        except Exception as e:
            failedBase = "failed_base"

        if not os.path.exists(location_cookies):
            os.makedirs(location_cookies)
        if not os.path.exists(location_uploads):
            os.makedirs(location_uploads)
        try:
            suffixes = config.get("OM_BASE", "suffixes").replace(' ', '').split(",")
        except Exception as e:
            suffixes = []
        try:
            includeStarts = str(config.get("OM_BASE", "includeStarts")).replace(' ', '').split(",")
            # print(includeStarts)
        except Exception as e:
            # print(e)
            includeStarts = "*"
        try:
            excludeStarts = str(config.get("OM_BASE", "excludeStarts")).replace(' ', '').split(",")
        except:
            excludeStarts = ""

        try:
            max_try = int(config.get("OM_BASE", "max_try"))
        except:
            max_try = -1
        try:
            max_upload = int(config.get("OM_BASE", "max_upload"))
        except:
            max_upload = -1
        try:
            single_publish = int(config.get("OM_BASE", "single_publish"))
        except:
            single_publish = -1
        try:
            single_max_try = int(config.get("OM_BASE", "single_max_try"))
        except:
            single_max_try = -1

        logging.info("本地视频文件基础目录：" + videoBase)
        logging.info("上传成功后的移动目的地：" + uploadedBase)
        logging.info("上传失败或取消后的移动目的地：" + failedBase)
        logging.info("允许的后缀为：%s" % suffixes)
        logging.info("排除的文件前缀为：" + str(excludeStarts))
        logging.info("有效的文件前缀为：" + str(includeStarts))


def start(file='account.xlsx', updateVideoInfo=False):
    global videoBase, excel_file, uploadedBase, failedBase, publish_interval, location_cookies, location_uploads, suffixes, includeStarts, excludeStarts, single_max_try
    tables = ExcelUtil.excel_table_byname(file=excel_file, colnameindex=2)
    for row in tables:
        logging.info("=========================== %s" % row)
        email = str(row["账号"])
        password = row["密码"]
        username = row["账号名称"]

        # email = "upqv97@163.com"
        # password = "qqq123qqq"

        category = row["领域"]    # 分类
        # category = "电影"   # 子分类
        subcategory = row["子分类"]    # "电影周边"   # 子分类
        publishCnt = row["发布数量"] # 系统限制每天只能发布5篇文章？？

        if 0 >= publishCnt:
            logging.warning(" 当前账户 " + username + " 不进行上传，因为 发布数量 = %d" % publishCnt)
            sess.close()
            continue

        # uploadCnt = row["上传数量"]
        tags = row["标签"]
        tags = tags.strip(" ") # 英文,
        tags = tags.replace("，", ",") # 中文，
        desc = row["描述"]
        userVideoBase = os.path.join(videoBase, username)
        if os.path.exists(userVideoBase):
            # userVideoBase = videoBase
            if not os.path.isdir(userVideoBase):
                logging.error("指定的视频存放路径不是一个有效目录：%s ！！" % userVideoBase)
                continue
        else:
            os.makedirs(userVideoBase)
            logging.warning("指定的视频存放路径不存在：%s !! 当前用户跳过上传过程！" % updateVideoInfo)
            continue

        sess = requests.session()
        sess.headers["User-Agent"] = base.useragent
        sess.headers["Referer"] = base.Referer
        sess.headers["Accept-Encoding"] = "gzip, deflate, br"
        sess.headers["Accept-Language"] = "zh-CN,zh;q=0.8"

        cookie = login.login(sess, email, password, location_cookies)
        if cookie :
            r = sess.get("https://om.qq.com/article/articlePublish")
            g_publish_status_ = "var g_publishStatus = {"
            lenx = len(g_publish_status_)
            ind1 = r.text.find(g_publish_status_)
            if ind1 > 0:
                ind2 = r.text.find("}", ind1 + lenx)
                if ind2 > 0:
                    g_publishStatus = r.text[ind1 + lenx - 1:ind2+1]
                    g_publishStatus_json = json.loads(g_publishStatus)
                    remain = g_publishStatus_json["videoRemain"]
                    if remain > 0:
                        logging.info("今日发文数剩余：%s" % remain)
                    elif remain <= 0:
                        logging.error("发布失败！今日发文数剩余：0. 可能今日发文数已超上限,，请改日再操作！")
                        # daylimit = '''var sfDailyLimit = "5";'''
                        # r.text.find(daylimit)
                        continue
            # return
            files = os.listdir(userVideoBase)
            fileCnt = len(files)
            if fileCnt <= 0:
                logging.warning(" 当前目录：%s 没有文件 !! " %userVideoBase)
                continue
            # if fileCnt > publishCnt:
            #     logging.info(" 当前目录文件数大于允许上传文件数 !! ")

            successCnt = 0
            uploadCnt = 0
            tryCnt = 0
            # remain = 1
            for file in files:
                tryCnt += 1

                if successCnt >= remain:
                    logging.info(" 当前账户"+ username+" ,成功发布文件数已达系统上限 ！")
                    sess.close()
                    break
                if 0 < single_max_try <= tryCnt:
                    logging.info(" 当前账户 " + username+" ,尝试上传文件数已达 cfg 设定上限 ！")
                    sess.close()
                    break
                if successCnt > 0 and successCnt >= publishCnt:
                    logging.info(" 当前账户"+ username+" ,成功发布文件数已达 Excel 设定上限 ！")
                    sess.close()
                    break

                # logging.info(file)
                local_file = os.path.join(userVideoBase, file)
                if not os.path.isfile(local_file):
                    # 如果不存在， 或者不是文件， 那么跳出循环
                    continue

                suffix = os.path.splitext(local_file)[1]
                if len(suffixes) != 0 and suffix not in suffixes:
                    # logging.info(" 文件后缀不正确， 可能不是视频文件！ ")
                    continue

                excluded = False
                ind = local_file.rfind("\\", 0)
                file_name = local_file[ind + 1:]
                # ind = file_name.rfind(".", 0)
                # title = file_name[0:ind]
                title = file_name

                for excludeStart in excludeStarts:
                    if file_name.startswith(excludeStart.strip(" ")):
                        logging.info(" 文件已经被排除 ！ " + file_name)
                        excluded = True
                        break

                if excluded:
                    continue

                included = False
                for includeStart in includeStarts:
                    # logging.info("type(includeStart", type(includeStart))
                    if includeStart == "*":
                        included = True
                        break
                    if file_name.startswith(includeStart.strip(" ")):
                        logging.info(" 文件属于白名单 ！ " + file_name)
                        included = True
                        break
                    else:
                        logging.info(" 文件 不 属于白名单 ！ " + file_name)

                if not included:
                    continue
                # sess.cookies.save();
                publishSuccess = False
                try:
                    uploadCnt += 1
                    video_file = open(local_file, 'rb')
                    # sys.exit()
                    # continue

                    if len(title) < 10:
                        logging.info("title 至少是  6个汉字，或6个单词")
                        continue
                    try:
                        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        # aid 表示 视频对应的文章id， 或者上传失败时候的错误代号， vid 就是视频id
                        userid = cookie.get("userid")
                        open_token = cookie.get("userid")
                        (aid, vid) = upload.upload(email, sess, userid, open_token, video_file,category, subcategory,tags)
                        time.sleep(publish_interval)

                        if isinstance(aid, int):
                            aid = int(aid)
                            if aid < 100:
                                publishSuccess = False
                        elif isinstance(aid, str):
                            publishSuccess = True
                            successCnt += 1

                        aid = str(aid).ljust(15, " ")
                        vid = str(vid).ljust(12, " ")

                        uploadRst = "vid:{vid}, aid:{aid}, fileName:{fileName}, date:{date}".format(vid=vid, aid=aid, fileName=file_name, date=now)
                        upload_file_name = os.path.join(location_uploads, email + ".upload.txt")

                        fd = open(upload_file_name, "a", encoding="utf-8")
                        # 写入字符串
                        fd.writelines(uploadRst+"\n")
                        # os.write(fd, "This is aaa")
                        # 关闭文件
                        fd.close()
                    except Exception as e:
                        logging.error("上传 失败！ " + str(e))
                        pass
                    sess.cookies.save()
                    # time.sleep(5)

                    # 暂时取消此方法
                    # duration = "0:00:00 "
                    # title = file_name + "" # title 至少是  6个汉字，或6个单词
                    # if len(title) < 10:
                    #     logging.info("title 至少是  6个汉字，或6个单词")
                    #     continue
                    #
                    # # title = urllib.request.quote(title)
                    # # tags = urllib.request.quote(tags)
                    # logging.info("")
                    # # logging.info(" 开始发布！ ")
                    # # # 格式：    "tags":"asd+wewe"
                    # # tags = "beta+err+gama+"
                    # tags = "beta+err+gama+" + tags
                    # pubResult = publish.publish(sess, vid, category, subcategory, desc, tags, duration, title)
                    # # sess.cookies.save();
                    #
                    # logging.info(pubResult)
                    # logging.info(" 发布结果！ " + pubResult)
                    # time.sleep(5)

                except Exception as e:
                    logging.error(e)
                finally:
                    video_file.close()
                    if publishSuccess:
                        # 剪切视频到“成功上传目录”
                        moveToUploaded(local_file, file_name, username)
                    else:
                        moveToUploadedFail(local_file, file_name, username)

                logging.info(" tryCnt  %d, successCnt  %d " % (tryCnt, successCnt))

                # if uploadCnt > 0 and uploadCnt >= max_publish:
                #     logging.info(" 当前账户"+ username+" ,成功发布文件数已达上限 ！")
                #     sess.close()
                #     break
            sess.close()

            # if successCnt < publishCnt:
            #     logging.info(" 当前账户", username, " ,成功发布文件数已达上限 ！")
            #     continue
            #   测试使用其他账号继续上传
            # break
        else:
            logging.error(email + "  "+  username +" 登录失败! ")
            sess.close()
            continue

# errr
def get_location_cookies():
    # global location_cookies
    if location_cookies:
        return location_cookies
    else:
        print(" get_location_cookies  ")
        return "cookies"

def moveToUploaded(local_file, file_name, username):
    logging.info("准备移动文件 %s ... " % local_file)
    uploadedDir = os.path.join(uploadedBase, username)
    if not os.path.exists(uploadedDir):
        os.makedirs(uploadedDir)

    uploadedTarget = os.path.join(uploadedDir, file_name)
    if not os.path.exists(uploadedTarget):
        shutil.move(local_file, uploadedTarget)
        logging.info("移动文件成功 ！ 从%s 到 %s" % (local_file, uploadedTarget))

def moveToUploadedFail(local_file, file_name, username):
    logging.info("No 准备移动文件 %s ... " % local_file)
    failedDir = os.path.join(failedBase, username)
    if not os.path.exists(failedDir):
        os.makedirs(failedDir)

    failedTarget = os.path.join(failedDir, file_name)
    # if not os.path.exists(failedTarget):
        # shutil.move(local_file, failedTarget)
        # logging.info("移动文件成功 ！ 从%s 到 %s" % (local_file, failedTarget))

		
if __name__ == '__main__':
    init()
    start(file='account.xlsx')
    # start(file='account.xlsx', updateVideoInfo=True)



