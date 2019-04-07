#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from Tools.snmp_getbulk import snmpv2_getbulk
from Tools.snmp_get import snmpv2_get
from pymongo import *
import numpy as np
from matplotlib_practice_line import mat_line

import time
import pprint
from datetime import datetime, timedelta

client = MongoClient('mongodb://qytangdbuser:python@192.168.11.100:27017/qytangdb')
db = client['qytangdb']


def get_int_info(ip, ro):
    if_name_list = [x[1] for x in snmpv2_getbulk(ip, ro, '1.3.6.1.2.1.2.2.1.2', count=25, port=161)]
    if_speed_list = [x[1] for x in snmpv2_getbulk(ip, ro, '1.3.6.1.2.1.2.2.1.5', port=161)]
    if_in_bytes = [x[1] for x in snmpv2_getbulk(ip, ro, '1.3.6.1.2.1.2.2.1.10', port=161)]
    if_out_bytes = [x[1] for x in snmpv2_getbulk(ip, ro, '1.3.6.1.2.1.2.2.1.16', port=161)]

    name_speed_in_out_list = zip(if_name_list, if_speed_list, if_in_bytes, if_out_bytes)

    all_info_dict = {}
    if_name_list = []

    for x in name_speed_in_out_list:
        if 'Ethernet' in x[0]:
            all_info_dict[x[0] + '_' + 'speed'] = x[1]
            all_info_dict[x[0] + '_' + 'in_bytes'] = int(x[2])
            all_info_dict[x[0] + '_' + 'out_bytes'] = int(x[3])
            if_name_list.append(x[0])
    all_info_dict.update({'if_name_list': if_name_list})

    # cpmCPUTotal5sec
    cpu_5s = int(snmpv2_get(ip, ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.3.7", port=161)[1])
    # cpmCPUMemoryUsed
    mem_u = int(snmpv2_get(ip, ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.12.7", port=161)[1])
    # cpmCPUMemoryFree
    mem_f = int(snmpv2_get(ip, ro, "1.3.6.1.4.1.9.9.109.1.1.1.1.13.7", port=161)[1])

    all_info_dict['ip'] = ip
    all_info_dict['cpu_5s'] = cpu_5s
    all_info_dict['mem_u'] = mem_u
    all_info_dict['mem_f'] = mem_f
    all_info_dict['record_time'] = datetime.now()

    return all_info_dict


def write_info_to_mongodb(device_info_dict):
    db.device_info.insert_one(device_info_dict)

    # for obj in db.device_info.find():
    #     pprint.pprint(obj, indent=4)


def read_info_from_mongodb(ifname, direction, last_mins):
    time_list = []
    if_bytes_list = []

    for x in db.device_info.find({'record_time': {'$gte': datetime.now() - timedelta(minutes=last_mins)}}):
        if_bytes_list.append(x[ifname + '_' + direction + '_bytes'])
        time_list.append(x['record_time'])

    print(time_list)
    print(if_bytes_list)
    diff_if_bytes_list = np.diff(if_bytes_list)
    # print(diff_if_bytes_list)
    diff_record_time_list = [x.seconds for x in np.diff(time_list)]
    # print(diff_record_time_list)
    speed_list = list(map(lambda x: round(((x[0] * 8) / (1000 * x[1])), 2), zip(diff_if_bytes_list, diff_record_time_list)))
    # print(speed_list)
    time_list = time_list[1:]
    # print(time_list)
    return time_list, speed_list


def delete_all():
    db.deiveinfo.remove()


def write_to_mongo_period(interval=5, seconds=120):
    while seconds > 0:
        write_info_to_mongodb(get_int_info('192.168.11.120', 'tcpipro'))
        time.sleep(interval)
        seconds -= interval


if __name__ == '__main__':
    write_to_mongo_period()
    x, y = read_info_from_mongodb('GigabitEthernet1', 'in', 2)
    print(x, y)
    title = '路由器{0}接口,{1}向,{2}分钟速率'.format('GigabitEthernet1', 'in', 2)
    mat_line(x, y, title, '采集时间', '速率kbps')



