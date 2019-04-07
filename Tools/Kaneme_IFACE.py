#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import logging
logging.getLogger("Kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
from GET_IFNAME import get_ifname
import platform


def kamene_iface(if_name):
    if platform.system() == 'Linux':
        return if_name
    elif platform.system() == 'Windows':
        for x,y in ifaces.items():
            # print(x,y)
            if y.pcap_name is not None:
                # print(y.pcap_name)
                if get_ifname(if_name) == ('{' + y.pcap_name.split('{')[1]):
                    return x
                else:
                    pass

if __name__ == "__main__":
    print(kamene_iface('Ethernet'))
