#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from pysnmp.hlapi import *
import datetime
import time
from pymongo import *
from matplotlib_practice_line import mat_line


def snmpv2_get(ip, community, oid, port=161):

    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))
               )
    )
    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus, errorIndex and varBinds[int(errorIndex)-1][0] or '?'
        )
              )
    result = ''

    for varBind in varBinds:

        result = result + varBind.prettyPrint()

    return result.split("=")[0].strip(), result.split("=")[1].strip()


def write_to_db(ip, community, seconds):
    client = MongoClient('mongodb://qytangdbuser:python@192.168.11.100:27017/qytangdb')
    db = client['qytangdb']

    while seconds > 0:
        mem_used = snmpv2_get(ip, community, '1.3.6.1.4.1.9.9.109.1.1.1.1.12.7')[1]
        mem_free = snmpv2_get(ip, community, '1.3.6.1.4.1.9.9.109.1.1.1.1.13.7')[1]
        mem_usage = (int(mem_used) / (int(mem_free) + int(mem_used))) * 100
        # print(type(mem_usage))
        # print(mem_usage)
        db.mem_usage_table.insert_one({'mem_percent': int(mem_usage), 'record_time': datetime.datetime.now()})
        time.sleep(5)
        seconds -= 5


def read_from_db():
    client = MongoClient('mongodb://qytangdbuser:python@192.168.11.100:27017/qytangdb')
    db = client['qytangdb']
    time_1 = datetime.datetime.now() - datetime.timedelta(minutes=1)
    print(time_1)
    # print(start_time)
    # print(end_time)

    time_list = []
    mem_percent_list = []

    for x in db.mem_usage_table.find({'record_time': {'$gte': time_1}}):
        time_list.append(x['record_time'])
        mem_percent_list.append(x['mem_percent'])

    return time_list, mem_percent_list


if __name__ == '__main__':
    write_to_db('192.168.11.120', 'tcpipro', 120)
    time_list, mem_percent_list = read_from_db()
    mat_line(time_list, mem_percent_list)

