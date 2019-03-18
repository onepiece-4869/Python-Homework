#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from Ping_class import *

ping = Qytangping('192.168.11.100')
print(ping)
ping.one()
ping.ping()


if __name__ == '__main__':
    pass

