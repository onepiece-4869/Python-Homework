#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from scapy_ping_one_new import qytang_ping
from paramiko_ssh import qytang_ssh


def ping_and_ssh(ip_list, username, password, cmd):
    for ip in ip_list:
        ping_result = qytang_ping(ip)
        if ping_result[1] == 1:
            print(ping_result[0], '可达!')
            print('登录', ping_result[0], '执行命令', cmd, '回显结果如下:')
            print(qytang_ssh(ping_result[0], username=username, password=password, cmd=cmd))
        else:
            print(ping_result[0], '不可达!')


if __name__ == '__main__':
    ip_list = ['192.168.220.129', '192.168.220.130']

    username = 'root'
    password = 'Cisc0123'

    ping_and_ssh(ip_list, username, password,'ls')
