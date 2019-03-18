#!/usr/bin/env python3
# -*- coding=utf-8 -*-


print('请输入一个英文单词')
word = input()
newword = word[1:] + '-' + word[0] + 'y'
print(newword)
