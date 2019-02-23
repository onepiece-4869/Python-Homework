#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import re

str1 = 'Port-channel1.189          192.168.189.254  YES     CONFIG   up                       up '

result = re.match('\s*(\w.*\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w*)\s+(\w*)\s+(\w*)\s+(\w*)\s*',str1).groups()

print(result)
print('-'*80)
print('%-7s : %s' % ('接口', result[0]))
print('%-7s : %s' % ('IP地址', result[1]))
print('%-7s : %s' % ('状态', result[-1]))