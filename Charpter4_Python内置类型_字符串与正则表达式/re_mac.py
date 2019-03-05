#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import re

str1 = '166    54a2.74f7.0326    DYNAMIC     Gi1/0/11'

result = re.match('(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\w+)\s+(\w.*\d)',str1).groups()

print('-'*80)
print('%-10s : %s' % ('VLAN ID', result[0]))
print('%-10s : %s' % ('MAC', result[1]))
print('%-10s : %s' % ('Type', result[2]))
print('%-10s : %s' % ('Interface', result[3]))