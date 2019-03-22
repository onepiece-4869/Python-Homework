#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
from GET_IP_netifaces import get_ip_address
from GET_MAC_netifaces import get_mac_address
from Kaneme_IFACE import kamene_iface
from GET_IFNAME import get_ifname


def arp_request(ip_address, ifname='ens33'):
    localip = get_ip_address(ifname)
    localmac = get_mac_address(ifname)
    try:
        result_raw = sr1(ARP(op=1, hwsrc=localmac, hwdst='00:00:00:00:00:00', psrc=localip, pdst=ip_address), iface=kamene_iface(ifname), timeout=1, verbose=False)
        return ip_address, result_raw.getlayer(ARP).fields['hwsrc']
    except AttributeError:
        return ip_address, None

if __name__ == "__main__":
    pass