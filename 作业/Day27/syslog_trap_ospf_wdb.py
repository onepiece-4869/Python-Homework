#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import socketserver
import re
from dateutil import parser
import os
import sqlite3

#
# class Facility:
#     KERN, USER, MAIL, DAEMON, AUTH, SYSLOG, LPR, NEWS, UUCP, CRON, AUTHPRIV, FTP = range(12)
#     LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7 = range(16,24)
#
#
# class Severity_Level:
#     EMERG, ALERT, CRIT, ERR, WARNING, NOTICE, INFO, DEBUG = range(8)

# facility与ID的对应关系的字典
facility_dict = {0: 'KERN',
                 1: 'USER',
                 2: 'MAIL',
                 3: 'DAEMON',
                 4: 'AUTH',
                 5: 'SYSLOG',
                 6: 'LPR',
                 7: 'NEWS',
                 8: 'UUCP',
                 9: 'CRON',
                 10: 'AUTHPRIV',
                 11: 'FTP',
                 16: 'LOCAL0',
                 17: 'LOCAL1',
                 18: 'LOCAL2',
                 19: 'LOCAL3',
                 20: 'LOCAL4',
                 21: 'LOCAL5',
                 22: 'LOCAL6',
                 23: 'LOCAL7'}

# severity_level与ID的对应关系的字典
severity_level_dict = {0: 'EMERG',
                       1: 'ALERT',
                       2: 'CRIT',
                       3: 'ERR',
                       4: 'WARNING',
                       5: 'NOTICE',
                       6: 'INFO',
                       7: 'DEBUG'}


class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = bytes.decode(self.request[0].strip())
        # print(data)
        if 'OSPF-5-ADJCHG' in str(data):
            ospf_info = re.match('.*OSPF-5-ADJCHG: Process (\d+), Nbr (\d+\.\d+\.\d+\.\d+) on (\w+\d+) from (\w+) to (\w+), .* ', str(data)).groups()
            print(f'OSPF Process {ospf_info[0]} Neighbor {ospf_info[1]} status {ospf_info[4]}')
        syslog_info_dict = {'device_ip': self.client_address[0]}
        syslog_info = re.match('^<(\d*)>(\d*): \*(.*): %(\w+)-(\d)-(\w+): (.*)', str(data)).groups()
        syslog_info_dict['facility'] = (int(syslog_info[0]) >> 3)
        syslog_info_dict['facility_name'] = facility_dict[int(syslog_info[0]) >> 3]
        syslog_info_dict['logid'] = int(syslog_info[1])
        syslog_info_dict['time'] = parser.parse(syslog_info[2])
        syslog_info_dict['log_source'] = syslog_info[3]
        syslog_info_dict['severity_level'] = (int(syslog_info[0]) & 0b111)
        syslog_info_dict['severity_level_name'] = severity_level_dict[(int(syslog_info[0]) & 0b111)]
        syslog_info_dict['description'] = syslog_info[5]
        syslog_info_dict['text'] = syslog_info[6]
        # print(syslog_info_dict)
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()
        cursor.execute("insert into syslogdb (time, \
                                              device_ip, \
                                              facility, \
                                              facility_name, \
                                              severity_level, \
                                              severity_level_name, \
                                              logid, \
                                              log_source, \
                                              description, \
                                              text) values ('%s', '%s', %d, '%s', %d, '%s', %d, '%s', '%s', '%s')" % (syslog_info_dict['time'].strftime("%Y-%m-%d %H:%M:%S"),
                                                                                                                     syslog_info_dict['device_ip'],
                                                                                                                     syslog_info_dict['facility'],
                                                                                                                     syslog_info_dict['facility_name'],
                                                                                                                     syslog_info_dict['severity_level'],
                                                                                                                     syslog_info_dict['severity_level_name'],
                                                                                                                     syslog_info_dict['logid'],
                                                                                                                     syslog_info_dict['log_source'],
                                                                                                                     syslog_info_dict['description'],
                                                                                                                     syslog_info_dict['text']
                                                                                                                     ))
        conn.commit()


if __name__ == '__main__':
    global dbname
    dbname = 'syslog.sqlite'
    if os.path.exists(dbname):
        os.remove(dbname)
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()

    cursor.execute("create table syslogdb(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                                             time varchar(64), \
                                             device_ip varchar(32),\
                                             facility int,\
                                             facility_name varchar(32),\
                                             severity_level int,\
                                             severity_level_name varchar(32),\
                                             logid int,\
                                             log_source varchar(32), \
                                             description varchar(128), \
                                             text varchar(1024)\
                                             )")
    conn.commit()

    try:
        HOST, PORT = "0.0.0.0", 514  # 本地地址与端口
        server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)  # 绑定本地地址，端口和syslog处理方法
        print("Syslog 服务已启用, 写入日志到数据库!!!")
        server.serve_forever(poll_interval=0.5)  # 运行服务器，和轮询间隔
    except (IOError, SystemExit):
        raise
    except KeyboardInterrupt:
        print('Crtl+C Pressed. Shutting down.')
    finally:
        conn.commit()