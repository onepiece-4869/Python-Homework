#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import json
from socket import *
import os
import base64
from Tools.paramiko_ssh import qytang_ssh


def Server_Jason(ip, port):
    # 创建TCP Socket, AF_INET为IPv4, SOCK_STREAM为TCP
    sockobj = socket(AF_INET, SOCK_STREAM)
    # 绑定套接字到地址，地址为（host, port）的元组
    sockobj.bind((ip, port))
    # 在拒绝连接前，操作系统可以挂起的最大连接数量，一般配置为5
    sockobj.listen(5)

    while True: # 一直接受请求，直到ctl+c终止程序
        try:
            # 接收TCP连接，并且返回（conn，address）的元组，conn为新的套接字对象，可以用来接收和发送数据，address是连接客户端的地址
            connection, address = sockobj.accept()
            # conn.settimeout(5.0)  # 设置连接超时!
            # 打印连接客户端的IP地址
            print('Server Connected by', address)
            received_message = b''
            received_message_fragment = connection.recv(1024)
            if len(received_message_fragment) < 1024:

                received_message = received_message_fragment
                obj = json.loads(received_message.decode())

            else:
                while len(received_message_fragment) == 1024:
                    received_message = received_message + received_message_fragment
                    received_message_fragment = connection.recv(1024)
                else:
                    received_message = received_message + received_message_fragment
                obj = json.loads(received_message.decode())

            if 'exec_cmd' in obj.keys():
                return_data = {'exec_cmd': os.popen(obj.get('exec_cmd')).read()}
            elif 'upload_file' in obj.keys():
                fp = open('upload_file.py', 'wb')
                fp.write(base64.b64encode(obj.get('file_bit').encode()))
                fp.close()
                print('上传文件{0}保存成功!'.format(obj.get('upload_file')))
                return_data = {'message': 'Upload Success!'}
            elif 'download_file' in obj.keys():
                file_bit = base64.b64encode(open(obj.  get('download_file'), 'rb').read()).decode()
                obj.update({'file_bit': file_bit})
                return_data = obj
            connection.send(json.dumps(return_data).encode())
            connection.close()
        except Exception as e:
            print(e)
            qytang_ssh('192.168.11.100', 'root', 'python', 'kill 6666')
        except KeyboardInterrupt:
            qytang_ssh('192.168.11.100', 'root', 'python', 'kill 6666')


if __name__ == '__main__':
    Server_IP = '0.0.0.0'
    Server_Port = 6666
    Server_Jason(Server_IP, Server_Port)

