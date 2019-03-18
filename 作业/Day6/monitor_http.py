#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import time
import os
import re


while True:
        netstat_result = os.popen('netstat -tulnp').read()
        # print(netstat_result)
        netstat_result_list = netstat_result.split('\n')
        netstat_result_list = netstat_result_list[2:]
        # print(netstat_result_list)
        for x in netstat_result_list:
            # print(x)
            if re.match('tcp\s+\d+\s+\d+\s*\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:(80)\s+.*\s+.*\s+.*', x.strip()):
                print('HTTP(TCP/80)服务已经被打开')
                break
        else:
            print('等一秒重新开始监控')
            time.sleep(1)
            continue
        break

