#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re


port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']

port_list_str = []
port_list_int = []
result_list = []
final_list = []
result = []

for x in port_list:
    a = re.match('\w+\s+(\d+)/(\d+)/(\d+)/(\d+)', x.strip()).groups()
    port_list_str.append(a)
# print(port_list_str)
for x in port_list_str:
    y = [int(i) for i in x]
    port_list_int.append(y)
# print(port_list_int)

result_list = sorted(port_list_int,key=lambda k:(k[0],k[1],k[2],k[[3]]))
# print(result_list)

for x in result_list:
    x = list(map(str,x))
    final_list.append(x)
# print(final_list)
for x in final_list:
    c = "/".join(x)
    line1 = 'eth ' + c
    result.append(line1)

for x in result:
    print(x)
print(result)