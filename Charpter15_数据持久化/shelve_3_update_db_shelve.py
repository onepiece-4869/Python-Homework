#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import shelve

db = shelve.open('people-shelve')
cq_bomb = db['cq_bomb']  #读取数据库键’cq_bomb’中的字典
cq_bomb['pay'] *= 1.6 #更新字典
db['cq_bomb'] = cq_bomb #把更新后的字典重新写回数据库键
db.close()
