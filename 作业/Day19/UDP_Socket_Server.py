#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import socket
import sys
import struct
import pickle
import hashlib

address = ('192.168.3.23', 6666)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(address)
print('UDP服务器就绪!等待客户数据!')
while True:
    try:
        recv_source_data = s.recvfrom(2048)
        recv_data, addr = recv_source_data
        # print(recv_data)
        udp_header = recv_data[:12]
        md5_recv = recv_data[-32:]
        recv_data_new = recv_data[12:-32]
        # print(pickle.loads(recv_data_new))
        # print(md5_recv)
        # print(udp_header)
        version, pkt_type, seq_id, length = struct.unpack('!HHLL', udp_header)
        # print(udp_header)
        # print(recv_data_new)
        m = hashlib.md5(udp_header + recv_data_new)
        md5_value = m.hexdigest()
        if md5_value.encode() == md5_recv:
            print('=' * 80)
            print('{0:<30}:{1:<30}'.format('数据来源于', str(addr)))
            print('{0:<30}:{1:<30}'.format('数据序号为', seq_id))
            print('{0:<30}:{1:<30}'.format('数据长度为', length))
            print('{0:<30}:{1:<30}'.format('数据内容为', str(pickle.loads(recv_data_new))))


    except KeyboardInterrupt:
        sys.exit()

s.close()