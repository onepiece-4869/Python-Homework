#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from get_router_config import write_config_md5_to_db
import sqlite3
from difflib import *
import smtplib, email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def read_from_db(dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute("select md5_config as md5_config,COUNT(*) as count from config_md5 group by md5_config")
    yourresults = cursor.fetchall()
    md5_list = []
    for i in yourresults:
        md5_list.append(i[0])
    print(md5_list)
    id_list = []
    for md5 in md5_list:
        cursor.execute("select id from config_md5 where md5_config = '%s'" % md5)
        yourresults = cursor.fetchall()
        for x in yourresults:
            id_list.append(x[0])
    id_list = sorted(id_list)
    # print(id_list)
    id_time_list = []
    for id in id_list:
        cursor.execute("select id, time from config_md5 where id = %d" % id)
        yourresults = cursor.fetchall()
        id_time_list.append(yourresults[0])
    for i in id_time_list:
        print('配置ID:', i[0], '配置时间:', i[1])

    print('请选择需要比较的配置ID:')
    id_1 = int(input('ID1:'))
    id_2 = int(input('ID2:'))

    cursor.execute("select config from config_md5 where id = %d" % id_1)
    yourresults = cursor.fetchall()
    id_1_config = yourresults[0][0]
    cursor.execute("select config from config_md5 where id = %d" % id_2)
    yourresults = cursor.fetchall()
    id_2_config = yourresults[0][0]

    txt_1 = id_1_config.split('\n')
    txt_2 = id_2_config.split('\n')
    # print(txt_1)
    result = Differ().compare(txt_1, txt_2)
    return_result = '\n'.join(list(result))
    return return_result

def qyt_smtp_attachment(mailserver, username, password, From, To, Subject, Main_Body, files=None):
    # 使用SSL加密SMTP发送邮件，此函数发送的邮件有主题，有正文，还可以发送附件
    Tos = To.split(';')
    Date = email.utils.formatdate()
    msg = MIMEMultipart()
    msg['Subject'] = Subject
    msg['From'] = From
    msg['To'] = To
    msg['Date'] = Date

    part = MIMEText(Main_Body)
    msg.attach(part)

    if files:
        for file in files:
            part = MIMEApplication(open(file, 'rb').read())
            part.add_header('Content-Dispostion', 'attachment', filename=file)
            msg.attach(part)

    server = smtplib.SMTP_SSL(mailserver, 465)
    server.login(username, password)
    failed = server.sendmail(From, Tos, msg.as_string())
    server.quit()

    if failed:
        print('Failed recipients:', failed)
    else:
        print('邮件已经成功发出')


if __name__ == '__main__':
    Main_Body = (read_from_db('qytangconfig.sqlite'))
    qyt_smtp_attachment('smtp.gmail.com',
                        '3348326959@qq.com',
                        'dmyymagcazklcjie',
                        '3348326959@qq.com',
                        '726128572@qq.com;xiaoyang429670@gmail.com',
                        '测试_配置差异',
                        Main_Body)

