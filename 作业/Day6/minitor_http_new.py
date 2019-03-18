#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import time
import os
import re

def monitor(port):

    while True:
        netstat_result = os.popen('netstat -tulnp').read()
        # print(netstat_result)
        netstat_result_list = netstat_result.split('\n')
        netstat_result_list = netstat_result_list[2:]
        # print(netstat_result_list)
        for x in netstat_result_list:
            print(x)
            a = re.match('tcp\s+\d+\s+\d+\s*(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)\s+.*\s+.*\s+.*\s*', x).groups()
            # print(a)
            if a[-1] == str(port):
                print(port,'HTTP(TCP/80)服务已经被打开')
                break
        else:
            print('等一秒重新开始监控')
            time.sleep(1)
            continue
        break

if __name__ == '__main__':
    monitor(80)

