#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from ping_one import qytang_ping
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool as PoolProcess
import ipaddress


def ping_scan(network):
    # 多线程
    # pool = ThreadPool(150)

    # 多进程
    pool = PoolProcess(150)
    net = ipaddress.ip_network(network)
    result_dict = {}
    for ip in net:
        result_ping = pool.apply_async(qytang_ping, args=(str(ip),))
        result_dict[str(ip)] = result_ping

    pool.close()
    pool.join()

    active_ip = []
    for ip, result in result_dict.items():
        if result.get()[1] == 1:
            active_ip.append(ip)
    return active_ip


if __name__ == '__main__':
    import pickle
    import datetime
    now = datetime.datetime.now()
    othertimeformat = now.strftime('%Y-%m-%d_%H-%M-%S')
    file_name = 'scan_save_pickle_{0}.pl'.format(othertimeformat)
    scan_file = open(file_name, 'wb')
    pickle.dump(ping_scan('192.168.11.0/24'), scan_file)
    scan_file.close()
    scan_file = open(file_name, 'rb')
    result_list = pickle.load(scan_file)
    print(result_list)

