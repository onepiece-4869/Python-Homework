#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re

str1 = """TCP Student  192.168.189.167:32806 Teacher  137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO 
TCP Student  192.168.189.167:80 Teacher  137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO """

result = str1.split(sep='\n')
D = {}
for x in result:
    result1 = re.match(
        '\w+\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+)\s+\w+\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+).*[bytes]\s+(\d+).*[flags]\s+(\w{3}).*',
        x).groups()
    keys = result1[0], result1[1], result1[2], result1[3]
    values = result1[4], result1[5]
    D[keys] = values

print('\n\n打印字典\n')
print(D)
print('\n\n格式化打印输出\n')

for keys, values in D.items():
    print('{0:>10} : {1:<20}'.format('src', keys[0]), '{0:>10} : {1:<10}'.format('src_p', keys[1]),
          '{0:>10} : {1:<15}'.format('dst', keys[2]), '{0:>10} : {1:<10}'.format('dst_p', keys[3]),
          '\n{0:>10} : {1:<20}'.format('bytes', values[0]), '{0:>10} : {1:<10}'.format('flags', values[1]), sep='|')
    # print('{0:>10} : {1:<20}'.format('src',keys[0]),'{0:>10} : {1:<10}'.format('src_p',keys[1]),'{0:>10} : {1:<15}'.format('dst',keys[2]),'{0:>10} : {1:<10}'.format('dst_p',keys[3]),sep='|')
    # print('{0:>10} : {1:<20}'.format('bytes',values[0]),'{0:>10} : {1:<10}'.format('flags',values[1]),sep='|')
    print('=' * 112)
