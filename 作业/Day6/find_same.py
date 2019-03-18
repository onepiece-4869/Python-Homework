#!/usr/bin/env python3
# -*- coding=utf-8 -*-


def find_same(a, b):
    for x in a:
        if x in b:
            print(x, 'in List1 and List2')
        else:
            print(x,  'only in List1')


if __name__ == '__main__':

    List1 = ['aaa', 111, (4, 5), 2.01]
    List2 = ['bbb', 333, 111, 3.14, (4, 5)]
    find_same(List1, List2)

