#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re

def list_sorted(post_list):
    port_list_str = []
    for x in port_list:
        a = re.match('\w+\s+(\d+)/(\d+)/(\d+)/(\d+)', x.strip()).groups()
        port_list_str.append(a)
    return port_list_str

def list_change(list2,a):
    port_list_change = []
    for x in list2:
        x = list(map(a, x))
        port_list_change.append(x)
    return port_list_change

def list_sort(list1):
    result_list = sorted(list1, key=lambda k:(k[0],k[1],k[2],k[3]))
    return result_list


if __name__ == '__main__':
    port_list = ['eth 1/101/1/42', 'eth 1/101/1/26', 'eth 1/101/1/23', 'eth 1/101/1/7', 'eth 1/101/2/46',]
                 'eth 1/101/1/34', 'eth 1/101/1/18', 'eth 1/101/1/13', 'eth 1/101/1/32', 'eth 1/101/1/25',
                 'eth 1/101/1/45', 'eth 1/101/2/8']
    result = []
    port_list_change = list_sorted(port_list)
    list1 = list_change(port_list_change, a=int)
    result_list = list_sort(list1)
    final_list = list_change(result_list, a=str)
    for x in final_list:
        c = "/".join(x)
        line1 = 'eth ' + c
        result.append(line1)

    for x in result:
        print(x)
    print(result)







