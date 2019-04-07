#!/usr/bin/env python3
# -*- coding=utf-8 -*-
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
colorlist = ['r', 'b', 'g', 'y']


def mat_zhu(size_list, name_list):
    # 调节图形大小，宽，高
    plt.figure(figsize=(6, 6))

    # 横向柱状图
    # plt.barh(name_list, size_list, height=0.5, color=colorlist

    # 纵向柱状图
    plt.bar(name_list, size_list, width=0.5, color=colorlist)

    # 添加主题和注释
    plt.title('协议与带宽分布')
    plt.xlabel('带宽(M/s)')
    plt.ylabel('协议')

    plt.savefig('result1.png')

    plt.show()


if __name__ == '__main__':
    size_list = [30, 53, 12, 45]
    name_list = ['http协议', 'ftp协议', 'rdp协议', 'QQ协议']
    mat_zhu(size_list, name_list)

