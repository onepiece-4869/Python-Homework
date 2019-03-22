#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from socket import inet_aton
import struct

IP_LIST = ['172.16.12.123',
           '172.16.12.3',
           '172.16.12.234',
           '172.16.12.12',
           '172.16.12.23'
           ]


def sort_ip(ips):
    return sorted(ips, key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])


if __name__ == '__main__':
    print(sort_ip(IP_LIST))

