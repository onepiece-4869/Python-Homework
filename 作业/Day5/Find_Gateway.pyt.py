#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import os

route_n_result = os.popen('route -n').read()
# print(type(route_n_result))
list_result = route_n_result.split('\n')
list_1 = list_result[2:-1]
result = []
for x in list_1:
    y = x.split()
    if y[3] == 'UG':
        print('网关为:' + y[1])