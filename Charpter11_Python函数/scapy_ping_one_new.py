#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def qytang_ping(ip):
    ping_pkt = IP(dst=ip) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return ip,1
    else:
        return ip,0


if __name__ == '__main__':
    result = qytang_ping('137.78.5.254')
    if result[1]:
        print(result[0], '通!')
    else:
        print(result[0], '不通!')
