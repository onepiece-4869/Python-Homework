#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re
import ipaddress


def full_ipv6(ipv6): #转换为完整的IPv6地址

    ipv6_section = ipv6.split(':') #对原始地址使用":"进行分割
    ipv6_section_len = len(ipv6.split(':')) #了解原始地址分段量
    if ipv6_section.index(''):
        null_location = ipv6_section.index('') #找到空位，这个地方要补0
        ipv6_section.pop(null_location) #把原来的空位弹出
        add_section = 8 - ipv6_section_len  + 1 #计算需要补'0000'的个数
        for x in range(add_section):
            ipv6_section.insert(null_location, '0000') #开始补0
        new_ipv6 = []
        for s in ipv6_section:
            if len(s) < 4:
                new_ipv6.append((4 - len(s)) * '0' + s) #对于长度不够的左边补0
            else:
                new_ipv6.append(s)
        return ':'.join(new_ipv6) #使用':'连接在一起
    else:
        return ipv6


def solicited_node_multicast_address(ipv6):
    return 'FE02::1:EF' + full_ipv6(ipv6)[-7:]


def mac_to_ipv6_linklocal(mac):

    mac_value = int(re.sub('[ :.-]', '', mac), 16)

    high2 = mac_value >> 32 & 0xffff ^ 0x0200

    high1 = mac_value >> 24 & 0xff

    low1 = mac_value >> 16 & 0xff

    low2 = mac_value & 0xffff


    return 'fe80::{0:04x}:{1:02x}ff:fe{2:02x}:{3:04x}'.format(high2, high1, low1, low2)

def ipv6_to_mac(ipv6):

    ipv6_address =  full_ipv6(ipv6)

    last_4_section = ipv6_address.split(':')[-4:]

    mac1 = int(last_4_section[0][:2], 16) ^ 0x02
    mac2 = int(last_4_section[0][2:], 16)
    mac3 = int(last_4_section[1][:2], 16)
    mac4 = int(last_4_section[2][2:], 16)
    mac5 = int(last_4_section[3][:2], 16)
    mac6 = int(last_4_section[3][2:], 16)

    return '{0:02x}:{1:02x}:{2:02x}:{3:02x}:{4:02x}:{5:02x}'.format(mac1, mac2, mac3, mac4, mac5, mac6)


def mac_to_eui64(mac, prefix):
    print()
    mac_value = int(re.sub('[ :.-]', '', mac), 16)
    print(mac_value)
    high2 = mac_value >> 32 & 0xffff ^ 0x0200

    high1 = mac_value >> 24 & 0xff

    low1 = mac_value >> 16 & 0xff

    low2 = mac_value & 0xffff

    host_id = '{0:04x}:{1:02x}ff:fe{2:02x}:{3:04x}'.format(high2, high1, low1, low2)

    net = prefix.split('/')[0]

    return net + host_id


if __name__ == "__main__":
    print(mac_to_eui64(mac='06:b2:4a:00:00:9f', prefix='2001:db8:100::/64'))
    print(mac_to_ipv6_linklocal('22:22:22:22:22:22'))
    print(solicited_node_multicast_address('2001::f107:94ac:2717:a736'))