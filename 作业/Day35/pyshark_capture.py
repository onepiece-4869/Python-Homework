#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import pyshark
from pymongo import *
import datetime

cap = pyshark.FileCapture('dos.pcap', keep_packets=False)
for pkt in cap:
    # print(pkt)
    pkt_dict = pkt.__dict__
    dict_1 = {}
    dict_2 = {}
    dict_3 = {}
    for layer in pkt_dict['layers']:
        layer_name = layer._layer_name
        for feild_name in layer.field_names:
            res = getattr(layer, feild_name)
            # print(res)
            dict_1[feild_name] = res
            # print(dict_1)
            dict_2[layer_name] = dict_1
            # print(dict_2)
    pkt_dict['layers'] = dict_2
    for feild_name in pkt_dict['frame_info'].field_names:
        res = getattr(pkt_dict['frame_info'], feild_name)
        dict_3[feild_name] = res
    pkt_dict['frame_info'] = dict_3
    # print(pkt_dict)


def write_to_db():
    global pkt_dict
    client = MongoClient('mongodb://qytangdbuser:python@192.168.11.100:27017/qytangdb')
    db = client['qytangdb']
    db.Capture.insert_one(pkt_dict)


# def read_from_db():
#     client = MongoClient('mongodb://qytangdbuser:python@192.168.11.100:27017/qytangdb')
#     db = client['qytangdb']
#     print(db.Capture.find())

# cap.apply_on_packets(print_highest_layer)

if __name__ == '__main__':
    write_to_db()
    # read_from_db()