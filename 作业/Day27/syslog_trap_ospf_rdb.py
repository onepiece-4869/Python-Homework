#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sqlite3
from netflow_matplotlib import mat_bing
from syslog_trap_ospf_wdb import severity_level_dict
# from syslog_trap_ospf_wdb import Severity_Level

def syslog_show(dbname):
    # 连接数据库
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    # 读取数据库
    # cursor.execute("select log_source as level,COUNT(log_source) as count from syslogdb group by log_source")
    cursor.execute("select severity_level as level,COUNT(severity_level) as count from syslogdb group by severity_level")
    yourresults = cursor.fetchall()

    level_list = []
    count_list = []

    # 把结果写入list
    for level_count in yourresults:
        level_list.append(severity_level_dict[level_count[0]])
        count_list.append(level_count[1])

    print(level_list)
    print([float(count) for count in count_list])

    return count_list, level_list


if __name__ == '__main__':
    count_list, level_list = syslog_show("syslog.sqlite")
    mat_bing(count_list, level_list)



