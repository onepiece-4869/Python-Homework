#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
from paramiko_ssh import qytang_ssh
import re


def mat_bing(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    #将某部分爆炸出来，使用括号，将第一块分割出来，数值的大小是分割出来的与其他两块的间隙
    # explode = （0.01, 0.01, 0.01, 0.01)

    patches, label_text, percent_text = plt.pie(size_list,
                                                labels=name_list,
                                                labeldistance=1.1,
                                                autopct='%3.1f%%',
                                                shadow=False,
                                                startangle=90,
                                                pctdistance=0.6)

    # labeldistance，文本的位置离原点有多远，1.1指1.1倍半径位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches，l_texts，p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    # 改变文本的大小
    # 方法是把每一个text遍历。调用set_size方法设置它的属性
    for l in label_text:
        l.set_size = 30
    for p in percent_text:
        p.set_size = 20
    # 设置x，y轴刻度一致，这样的饼图才能是圆的
    plt.axis('equal')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    result_show = qytang_ssh('192.168.11.120', 'admin', 'cisco', cmd='show flow monitor name qytang-monitor  cache format table')
    print(result_show)
    result_show = result_show.split('\n')
    result_show = [x for x in result_show if x != '' and x != ' ']
    counters = []
    protocols = []
    protocols_new = []
    for x in result_show:
        if re.findall('APP NAME', x):
            a = result_show.index(x)
            result_show_new = result_show[12:]
            # print(result_show_new)
    for x in result_show_new:
        if re.match('(\w+\s*\w+)\s+(\d+)\r', x).groups():
            b = re.match('(\w+\s*\w+)\s+(\d+)\r', x).groups()
            counters.append(b[1])
            protocols.append(b[0])
    for x in protocols:
        # print(x)
        if re.findall('port', x):
            x = x[5:]
            protocols_new.append(x)
        else:
            protocols_new.append(x)
    # print(protocols)
    mat_bing(counters, protocols_new)




