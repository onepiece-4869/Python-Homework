#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import time

while True:
    try:  # 尝试去执行
        time.sleep(2)
        print('请输入Ctrl + C来停止这个循环')
    except KeyboardInterrupt:
        # 如果出现KeyboardInterrupt异常的处理方法
        print("接收到管理员的ctrl+c!")
        print("退出程序")
        break
