#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import re
import os

route_n_result = os.popen("route -n").read()
#print(route_n_result)

route_n_result_list = route_n_result.split('\n')

#print(route_n_result_list)

route_n_result_list = route_n_result_list[2:-1]

#print(route_n_result_list)

for x in route_n_result_list:
    if x.split()[3] == 'UG':
        print('网关为:' + x.split()[1])

