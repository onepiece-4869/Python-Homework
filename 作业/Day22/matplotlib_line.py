#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'


def mat_line(time_list, mem_list):
    # 调节图形大小，宽，高
    fig = plt.figure(figsize=(6, 6))
    # 一共一行，每行一图，第一图
    ax = fig.add_subplot(111)

    # 处理X轴时间格式
    import matplotlib.dates as mdate
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%H:%M'))

    # 处理Y轴百分比格式
    import matplotlib.ticker as mtick
    ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%d%%'))

    # 把cpu_usage_list的数据，拆分为x轴的时间，与y轴的利用率
    x = []
    y = []

    for time, cpu in cpu_usage_list:
        x.append(time)
        y.append(cpu)

    # 添加主题和注释
    plt.title('路由器CPU利用率')
    plt.xlabel('采集时间')
    plt.ylabel('CPU利用率')

    fig.autofmt_xdate()  # 当x轴太拥挤的时候可以让它自适应

    # 实线红色
    ax.plot(x, y, linestyle='solid', color='r', label='R1')
    # 虚线黑色
    # ax.plot(x, y, linestyle='dashed', color='b', label='R1')

    # 如果你有两套数据，完全可以在一幅图中绘制双线
    # ax.plot(x2, y2, linestyle='dashed', color='b', label='R2')

    # 设置说明的位置
    ax.legend(loc='upper left')

    # 保存到图片
    plt.savefig('result1.png')
    # 绘制图形
    plt.show()


if __name__ == '__main__':
    import random
    import datetime
    cpu_usage_list = []
    for i in range(-12, 13):
        # print(i)
        time = datetime.datetime.now() + datetime.timedelta(hours=i)
        cpu_usage_list.append((time, random.randint(0, 100)))
    mat_line(cpu_usage_list)


