#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *


def qytang_ping(ip):
    ping_packet = IP(dst=ip)/ICMP()
    # ping_result = sr1(ping_packet, timeout=1, verbose=False)
    ping_result = sr1(ping_packet, timeout=2, verbose=False)
    if ping_result:
        return 1
    else:
        return 0


if __name__ == '__main__':
    print('请输入IP地址:')
    test_ip = input()
    if qytang_ping(test_ip):
        print(test_ip, '通!')
    else:
        print(test_ip, '不通!')



