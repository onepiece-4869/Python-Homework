#!/usr/bin/env python3
# -*- coding=utf-8 -*-


from paramiko_ssh import qytang_ssh
import sqlite3
import re
import hashlib

conn = sqlite3.connect('qytangconfig.sqlite')
cursor = conn.cursor()
cursor.execute("create table config_md5 (ip varchar(40), config varchar(99999), md5_config varchar(999))")

device_list = ['192.168.11.120']

username = 'admin'
password = 'cisco'


def get_config_md5(ip, username, password):
    run_config_raw = qytang_ssh(ip, username, password)
    where = run_config_raw.find('hostname')
    run_config_raw = run_config_raw[where:]
    # print(show_run)
    run_config_raw = re.split('\r*\n+!*', run_config_raw)
    run_config_raw = [x for x in run_config_raw if x != '' and x != ' ']
    run_config_new = '\n'.join(run_config_raw)

    m = hashlib.md5()
    m.update(run_config_new.encode())
    md5_value = m.hexdigest()
    # print(run_config_new)
    return run_config_new, md5_value


def write_config_md5_to_db():
    conn = sqlite3.connect('qytangconfig.sqlite')
    cursor = conn.cursor()
    for device in device_list:
        config_and_md5 = get_config_md5(device, username, password)
        cursor.execute("select md5_config from config_md5 where ip = '%s'" % device)
        md5_results = cursor.fetchall()
        if not md5_results:
            cursor.execute("insert into config_md5 values ('%s', '%s', '%s')" % (device, config_and_md5[0], config_and_md5[1]))
        elif config_and_md5[1] != md5_results[0]:
            cursor.execute("update config_md5 set md5_config = '%s' where ip = '%s'" % (config_and_md5[1], device))
        else:
            pass
    cursor.execute("select * from config_md5")
    all_results = cursor.fetchall()
    for x in all_results:
        print(x[0], x[2])

    conn.commit()


if __name__ == '__main__':
    # print(get_config_md5('192.168.11.120', 'admin', 'cisco'))
    write_config_md5_to_db()
