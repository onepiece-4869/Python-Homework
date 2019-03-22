#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import netifaces as ni
import winreg as wr

def get_connecton_name_from_guid(iface_guids):
    iface_dict = {}
    reg = wr.ConnectRegistry(None, wr.HKEY_LOCAL_MACHINE)
    reg_key = wr.OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}')
    for i in range(len(iface_guids)):
        try:
            reg_subkey = wr.OpenKey(reg_key, iface_guids[i] + r'/Connection')
            iface_dict = [wr.QueryValueEx(reg_subkey, 'Name')[0]] = iface_guids[i]
        except FileNotFoundError:
            pass

    return iface_dict

def win_from_name_get_id(ifname):
    x = ni.interfaces()
    return get_connecton_name_from_guid(x).get(ifname)


if __name__ == "__main__":
    print(win_from_name_get_id('Wi-Fi'))