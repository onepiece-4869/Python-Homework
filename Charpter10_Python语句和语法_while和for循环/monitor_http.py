#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import re
import os
import time
while True:
    monitor_result = os.popen("netstat -tulnp").read()

    monitor_result_list = monitor_result.split('\n')

    monitor_result_list = monitor_result_list[2:-1]

    #print(monitor_result_list)

    for x in monitor_result_list:
        if x.split()[3].split(':')[-1] == '80':
            print('HTTP（TCP/80）服务已经被打开')
            break
    else:
        print('等待一秒重新开始监控！')
        time.sleep(1)
        continue
    break