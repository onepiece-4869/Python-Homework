#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from pysnmp.hlapi import *
import datetime
import time
import pg8000
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


def write_to_db(ip, community, db, seconds):
    conn = pg8000.connect(host='192.168.11.100', user='qytangdbuser', password='python', database=db)
    cursor = conn.cursor()
    # cursor.execute("create table routerdb(id SERIAL PRIMARY KEY, record_time timestamp default current_timestamp, mem_percent int)")

    while seconds > 0:
        mem_used = snmpv2_get(ip, community, '1.3.6.1.4.1.9.9.109.1.1.1.1.12.7')[1]
        mem_free = snmpv2_get(ip, community, '1.3.6.1.4.1.9.9.109.1.1.1.1.13.7')[1]
        mem_percent = (int(mem_used) / (int(mem_free) + int(mem_used))) * 100
        cursor.execute("insert into routerdb (mem_percent) values (%d)" % int(mem_percent))
        time.sleep(5)
        seconds -= 5
    cursor.execute("select * from routerdb")
    yourresults = cursor.fetchall()
    for i in yourresults:
        print(i)
    conn.commit()


def read_from_db(db):
    conn = pg8000.connect(host='192.168.11.100', user='qytangdbuser', password='python', database=db)
    cursor = conn.cursor()
    cursor.execute("select record_time from routerdb order by record_time desc limit 1")
    yourresult = cursor.fetchall()
    time_1 = yourresult[0][0] - datetime.timedelta(minutes=1)
    cursor.execute("select record_time, mem_percent from routerdb WHERE record_time >= '{0}'".format(time_1))
    yourresults = cursor.fetchall()
    print(yourresults)

    time_list = []
    mem_percent_list = []

    for time_mem in yourresults:
        time_list.append(time_mem[0])
        mem_percent_list.append(time_mem[1])

    print(time_list)
    for x in time_list:
        print(x)
    print(mem_percent_list)
    return time_list, mem_percent_list


if __name__ == '__main__':
    write_to_db('192.168.11.120', 'tcpipro', 'qytangdb', 120)
    time_list, mem_percent_list = read_from_db('qytangdb')
    mat_line(time_list, mem_percent_list)

