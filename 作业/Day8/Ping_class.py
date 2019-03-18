#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging

logging.getLogger("kamane.runtime").setLevel(logging.ERROR)
from kamene.all import *


class Qytangping:

    def __init__(self, ip):
        self.ip = ip
        self.srcip = None
        self.length = 100
        self.packet = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)
        self.print_str1 = None
        self.print_str2 = None

    def src(self, srcip):
        self.srcip = srcip
        self.packet = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def size(self, length):
        self.length = length
        self.packet = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.length)

    def one(self):
        result = sr1(self.packet, timeout=1, verbose=False)
        if result:
            print(self.ip, '可达!')
        else:
            print(self.ip, '不可达!')

    def ping(self, print_str1='!', print_str2='.'):
        self.print_str1 = print_str1
        self.print_str2 = print_str2
        for i in range(5):
            result = sr1(self.packet, timeout=1, verbose=False)
            if result:
                print(print_str1, end='', flush=True)
            else:
                print(print_str2, end='', flush=True)

    def __str__(self):
        return '<srcip:%s,dstip:%s,size=%d>' % (self.srcip, self.ip, self.length)


class Newping(Qytangping):

    def ping(self, print_str3='+', print_str4='?'):
        Qytangping.ping(self, print_str3, print_str4)


if __name__ == '__main__':
    pass

