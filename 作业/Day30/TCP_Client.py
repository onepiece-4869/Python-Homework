#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import json
from socket import *
import base64


def Client_JSON(ip, port, obj):
    # 创建TCP Socket开连接
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.connect((ip, port))

    if 'exec_cmd' in obj:
        send_obj = obj
    elif 'upload_file' in obj:
        file_name = obj.get('upload_file')
        file_bit = base64.b64encode(open(file_name, 'rb').read())
        obj.update({'file_bit':file_bit.decode()})
        send_obj = obj
    elif 'download_file' in obj:
        send_obj = obj

    # 把obj转换为JSON字节字符串
    send_message = json.dumps(send_obj).encode()
    # 读取1024字节长度数据，准备发生数据分片
    send_message_fragment = send_message[:1024]
    # 剩余数据部分
    send_message = send_message[1024:]

    while send_message_fragment:
        sockobj.send(send_message_fragment) # 发送数据分片（如果分片的话）
        send_message_fragment = send_message[:1024] # 读取1024字节长度数据
        send_message = send_message[1024:] # 剩余数据部分

    received_message = b'' # 预先定义接受信息变量
    received_message_fragment = sockobj.recv(1204) # 读取接收到的信息，写入到接收到信息分片

    while received_message_fragment:
        received_message = received_message + received_message_fragment
        received_message_fragment = sockobj.recv(1024)

    return_data = json.loads(received_message.decode())
    if 'download_file' not in return_data.keys():
        print('接收确认数据:', return_data)
    else:
        print('收到确认数据:', return_data)
        fp = open('download_file.py', 'wb')
        fp.write(base64.b64decode(return_data.get('file_bit').encode()))
        fp.close()
        print('下载文件{0}保存成功!'.format(return_data.get('download_file')))


if __name__ == '__main__':
    port = 6666
    exec_cmd = {'exec_cmd': 'pwd'}
    Client_JSON('192.168.11.100', port, exec_cmd)
    upload_file = {'upload_file': 'snmp_get.py'}
    Client_JSON('192.168.11.100', port, upload_file)
    download_file = {'download_file': 'snmp_get.py'}
    Client_JSON('192.168.11.100', port, download_file)

