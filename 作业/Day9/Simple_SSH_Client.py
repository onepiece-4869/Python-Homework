#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from paramiko_ssh import qytang_ssh


if __name__ == '__main__':
    from argparse import ArgumentParser

    usage = 'usage:python Simple_SSH_Client -i ipaddr -u username -p password -c command'

    parser = ArgumentParser(usage)

    parser.add_argument("-i", "--ipaddr", dest='ipaddr', help='SSH Server', default='192.168.11.40')
    parser.add_argument("-u", "--username", dest='username', help='SSH Username', default='admin')
    parser.add_argument("-p", "--password", dest='password', help='SSH Password', default='root')
    parser.add_argument("-c", "--command", dest='command', help='Shell Command', default='pwd')

    a = parser.parse_args()

    print(qytang_ssh(a.ipaddr, a.username, a.password, a.command))




