#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import time
import os
import threading

def qyt_multi(x,y,z):
    #打印进程和线程ID
    #print('pid tid ==>',os.getpid(),threading.currentThread().ident)
    i = 1
    while i < 10:
        sum = x * y * z
        x += 1
        y += 1
        z += 1
        i += 1
        time.sleep(1)
    # 返回计算结果，进程号，线程号
    return (sum, os.getpid(), threading.currentThread().ident)

if __name__ == '__main__':
    print(qyt_multi(1,2,3))