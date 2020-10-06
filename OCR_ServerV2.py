# @Author  :  lijishi
# @Contact :  lijishi@emails.bjut.edu.cn
# @Software:  Pycharm & Python 2.7
# @EditTime:  Oct 6, 2020
# @Version :  2.0
# @describe:  Confirm Availability of Text Identify --Server
# @LICENSE :  GNU GENERAL PUBLIC LICENSE Version 3

# Deploy On Tencent Cloud Serverless

# -*- coding: utf8 -*-
import time
import datetime
import pymysql.cursors
import logging
import sys
import pytz
import json

# MySql database account information, you need to create a database in advance. MySql数据库账号信息,需要提前创建好数据库
Host = 'DB Address'
User = 'Account'
Password = 'Password'
Port = 3306
DB = u'DB Name'

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger()
logger.setLevel(level=logging.INFO)

# Changing the time zone to Beijing. 更改时区为北京时区
tz = pytz.timezone('Asia/Shanghai')

g_connection = None
g_connection_errno = 0


def connect_mysql():
    global g_connection
    global g_connection_errno
    try:
        g_connection = pymysql.connect(host=Host,
                                       user=User,
                                       password=Password,
                                       port=Port,
                                       db=DB,
                                       charset='utf8',
                                       cursorclass=pymysql.cursors.DictCursor)
    except Exception as e:
        g_connection = None
        g_connection_errno = e[0]
        print("connect database error:%s" % e)


# print("connect database")

def main_handler(event, context):
    global g_connection
    connect_mysql()

    url = event['path'][5:-1]
    param = url.split('+')
    if param[0] == '1':  # query
        ym = datetime.datetime.now(tz).strftime("%Y-%m")
        applynum = int(param[1])
        sql = 'SELECT COUNT(tm) FROM log WHERE isok = 1 and apply = ' + str(applynum) + ' and time = \'' + str(ym) + '\''
        with g_connection.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
        querynum = res[0]['COUNT(tm)']
        # return str(sql)
        return querynum
    elif param[0] == '2':  # write
        tm = int(time.time())
        ym = datetime.datetime.now(tz).strftime("%Y-%m")
        applynum = int(param[1])
        key = param[2]

        sql = 'SELECT COUNT(tm) FROM log WHERE isok = 1 and apply = ' + str(applynum) + ' and time = \'' + str(ym) + '\''
        with g_connection.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
        querynum = res[0]['COUNT(tm)']
        if querynum < 1000:
            leftnum = 1000 - int(querynum) - 1
        else:
            leftnum = 0

        leftflag = 0
        keyflag = 0
        if key == '1234567' or key == 'lijishi':
            if int(leftnum) > 0:
                isok = 1
            else:
                isok = 0
                leftflag = 1
        else:
            isok = 0
            keyflag = 1
        sql = 'INSERT INTO log VALUES (' + str(tm) + ', \'' + str(ym) + '\', ' + str(applynum) + ', \'' + str(key) + '\', ' + str(isok) + ')'
        with g_connection.cursor() as cursor:
            cursor.execute(sql)
            res = cursor.fetchall()
            g_connection.commit()
            cursor.close()
        # return str(sql)
        if keyflag == 1:
            return '2+101'
        elif leftflag == 1:
            return '2+102'
        else:
            return '1+' + str(leftnum)

    # sql = 'SELECT COUNT(avid) FROM bili_video_data WHERE avid >= 50000000 and avid < 75000000'

    if not g_connection:
        connect_mysql()
        if not g_connection:
            return {"code": 409, "errorMsg": "internal error %s" % g_connection_errno}

    with g_connection.cursor() as cursor:
        cursor.execute(sql)
        res = cursor.fetchall()

        cursor.close()

    return str(str(url) + ', ' + str(res[0]['COUNT(avid)'])) + ', ' + str(datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S"))
