#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from kamene_ping import qytang_ping
from paramiko_ssh import qytang_ssh


def qytang_remote_login(ip):
    for x in ip:
        if qytang_ping(x):
            print(x, '通!')
            print(qytang_ssh(x, username='root', password='python'))
        else:
            print(x, '不通!')


if __name__ == '__main__':

    ip = ['192.168.11.100', '2.2.2.2']
    username = 'root'
    password = 'python'
    qytang_remote_login(ip)

