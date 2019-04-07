#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from datetime import datetime
import logging
# 记录日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s%(filename)s[line:%(lineno)d]%(levelname)s%(message)s', datefmt='%Y-%m-%d %H:%M:%S', filename='log1.txt', filemode='a')

# 测试函数 # 可以换为import的获取路由器配置并写入数据库的脚本


def qyt_print(x,y):
    print('测试答应信息!', x, y)
    # print(1/0) # 制造错误


def my_listener(event):
    # 获取job_id
    job_id = event.job_id

    if event.exception:
        debug_message = event.traceback
        print(job_id + '执行错误!')
        print('错误信息如下:')
        print(debug_message)

    else:
        print(job_id + '正常执行!')


scheduler = BlockingScheduler()
scheduler.add_job(func=qyt_print, args=['test1', 'test2'], trigger='interval', seconds=10, start_date=datetime(2019, 3, 27, 23, 18), end_date=datetime(2019, 3, 27, 23, 19), id='interval调度!测试正常打印!')
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler._logger = logging
scheduler.start()


if __name__ == '__main__':
    pass

