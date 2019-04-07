#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import logging

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
import re
from kamene.all import *
from Tools.Kaneme_IFACE import kamene_iface

qyt_string = b''


def reset_tcp(pkt):
    source_mac = pkt[Ether].fields['src']
    destination_mac = pkt[Ether].fields['dst']
    source_ip = pkt[IP].fields['src']
    destination_ip = pkt[IP].fields['dst']
    source_port = pkt[TCP].fields['sport']
    destination_port = pkt[TCP].fields['dport']
    seq_sn = pkt[TCP].fields['seq']
    ack_sn = pkt[TCP].fields['ack']

    a = Ether(src=source_mac, dst=destination_mac) / IP(src=source_ip, dst=destination_ip) / TCP(dport=destination_port,
                                                                                                 sport=source_port,
                                                                                                 flags=4, seq=seq_sn)
    b = Ether(src=destination_mac, dst=source_mac) / IP(src=destination_ip, dst=source_ip) / TCP(dport=source_port,
                                                                                                 sport=destination_port,
                                                                                                 flags=4, seq=ack_sn)

    sendp(a, iface=global_if, verbose=False)
    sendp(b, iface=global_if, verbose=False)


def telnet_monitor_callback(pkt):

    global qyt_string
    try:
        if pkt.getlayer(TCP).fields['dport'] == 23:
            if pkt.getlayer(Raw).fields['load'].decode():
                qyt_string = qyt_string + pkt.getlayer(Raw).fields['load']
    except:
        pass

    if re.match(b'(.*\r\n.*)*sh.*\s+run.*', qyt_string):
        reset_tcp(pkt)


def telnet_rst(user_filter, ifname):
    global global_if
    global_if = kamene_iface(ifname)
    print(global_if)
    PTKS = sniff(prn=telnet_monitor_callback,
                 filter=user_filter,
                 store=1,
                 iface=global_if,
                 timeout=10)
    try:
        wrpcap("qytang_day18.pcap", PTKS)
    except:
        pass
    print(qyt_string)


if __name__ == '__main__':
    while True:
        telnet_rst('tcp port 23 and ip host 192.168.11.120', 'Ethernet')

