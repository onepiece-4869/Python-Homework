#!/usr/bin/env python3
# -*- coding=utf-8 -*-


import re

str1 = 'Port-channel1.189          192.168.189.254  YES     CONFIG   up                       up '

# result = re.match('(\w+-*\w+\.\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+(up|down)\s+(up|down)',str1.strip()).groups()
# if result[2] == 'up' and result[3] == 'up':
#     status = 'up'
#
#
# # print(result)
#
#
# print_result = '{0:<10}: {1:<20}\n{2:<10}: {3:<20}\n{4:<10}: {5:<20}'.format('接口',result[0],'IP地址',result[1],'状态',status)
#
# print('-'*40)
# print(print_result)

result = re.match('(\w+-?\w*)(\d+)\.(\d+).*',str1).groups()
print(result)
