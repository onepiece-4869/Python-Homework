#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from pysnmp.hlapi import *
import sqlite3
import os
import datetime
import time
from dateutil import parser


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
    if os.path.exists(db):
        os.remove(db)
    conn = sqlite3.connect('MEM_usage_SNMP.sqlite')
    cursor = conn.cursor()
    cursor.execute("create table routerdb(id INTEGER PRIMARY KEY AUTOINCREMENT, time varchar(64), mem_percent int)")

    while seconds > 0:
        mem_used = snmpv2_get(ip, community, '1.3.6.1.4.1.9.9.109.1.1.1.1.12.7')[1]
        mem_free = snmpv2_get(ip, community, '1.3.6.1.4.1.9.9.109.1.1.1.1.13.7')[1]
        mem_percent = (int(mem_used) / (int(mem_free) + int(mem_used))) * 100
        time_info = datetime.datetime.now()
        cursor.execute("insert into routerdb (time, mem_percent) values ('%s', %d)" % (time_info, int(mem_percent)))
        time.sleep(5)
        seconds -= 5
    conn.commit()


def read_from_db(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    cursor.execute("select time, mem_percent from routerdb")
    yourresults = cursor.fetchall()
    print(yourresults)

    time_list = []
    mem_percent_list = []


    for time_mem in yourresults:
        time_1 = datetime.datetime.now() - datetime.timedelta(minutes=1)
        if parser.parse(time_mem[0]) > time_1:
            time_list.append(parser.parse(time_mem[0]))
            mem_percent_list.append(time_mem[1])

    print(time_list)

    return time_list, mem_percent_list


def mat_cpu_line(time_list, mem_percent_list):

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdate
    import matplotlib.ticker as mtick

    f, ax = plt.subplots(1)


    ax.xaxis.set_major_formatter(mdate.DateFormatter("%H:%M:%S"))
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

    ax.plot(time_list, mem_percent_list, linestyle='dashed', color='r')
    ax.set_ylim(bottom=0, top=100)

    plt.show()


if __name__ == '__main__':
    write_to_db('192.168.11.120', 'tcpipro', 'MEM_usage_SNMP.sqlite', 120)
    time_list, mem_percent_list = read_from_db('MEM_usage_SNMP.sqlite')
    mat_cpu_line(time_list, mem_percent_list)

