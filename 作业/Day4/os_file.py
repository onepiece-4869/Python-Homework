#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import os
import re
import shutil


os.mkdir('test')
os.chdir('test')
qytang1 = open('qytang1','w')
qytang1.write('test file\n')
qytang1.write('this is qytang\n')
qytang1.close()
qytang2 = open('qytang2','w')
qytang2.write('test file\n')
qytang2.write('qytang python\n')
qytang2.close()
qytang3 = open('qytang3','w')
qytang3.write('test file\n')
qytang3.write('this is python\n')
qytang3.close()
os.mkdir('qytang4')
os.mkdir('qytang5')
file_find_list = []
filelist = os.listdir()
for x in filelist:
    if os.path.isfile(x):
        for y in open(x,'r'):
            if re.findall('qytang',y):
                file_find_list.append(x)

        # y = open(x,'r').read()
        # if 'qytang' in y:
        #     file_find_list.append(x)

line1 = '文件中包含“qytang"关键字的文件为:'
print(line1)
for z in file_find_list:
    print('{0:^21}'.format(z))

os.chdir('..')
shutil.rmtree('test')






