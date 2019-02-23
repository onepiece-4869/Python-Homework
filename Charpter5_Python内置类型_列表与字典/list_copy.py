#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

l1 = [4,5,7,1,3,9,0]

l2 = l1[:]

l2.sort()

for i in range(len(l1)):
	print(l1[i],l2[i])