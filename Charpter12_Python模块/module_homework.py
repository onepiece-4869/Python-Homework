#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from scapy_ping_one_new import scapy_ping_one
from paramiko_ssh import paramiko_ssh


def ping_and_ssh(ip_list, username, password, cmd):
    for ip in ip_list:
        ping_result = scapy_ping_one(ip)
        if ping_result[1] == 1:
            print(ping_result[0],'可达！')
            print('登录',ping_result[0], '执行命令', cmd, '回显结果如下:')
            print(paramiko_ssh(ping_result[0], username=username, password=password, cmd=cmd))
        else:
            print(ping_result[0],'不可达！')


if __name__ == '__main__':
    ip_list = ['172.16.1.102', '172.16.1.111']

    username = 'root'
    password = 'Cisc0123'

    ping_and_ssh(ip_list, username,password, 'ls')