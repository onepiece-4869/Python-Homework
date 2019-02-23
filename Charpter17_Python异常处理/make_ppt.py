#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a


import os

os.chdir(r'G:\资料\PyCharmProjects\Python基础课\image\PPT\Charpter17')

filelist = os.listdir()

maxno = len(filelist)

os.chdir(r'G:\资料\PyCharmProjects\Python基础课\Charpter17_Python异常处理')

#print(open('本章PPT.md','rb').read())
pptfile = open('本章PPT.md','w')

for i in range(maxno):
    pptfile.write('![](https://gitee.com/qytanggit/Python_Basic/raw/master/image/PPT/Charpter17/'+ str(i+1) + '.PNG)\r\n\r\n')

pptfile.close()

