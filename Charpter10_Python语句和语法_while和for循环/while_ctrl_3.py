#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import time
import signal
import sys


def sigint_handler(signum, frame):  # 定义处理方法
    print("接收到管理员的ctrl+c!")
    print("退出程序")
    sys.exit()


signal.signal(signal.SIGINT, sigint_handler)
# 定义了收到’ctl+c’（SIGINT）这个信号后的处理方法为sigint_handler
while True:
    time.sleep(2)
    print('请输入Ctrl + C来停止这个循环')
