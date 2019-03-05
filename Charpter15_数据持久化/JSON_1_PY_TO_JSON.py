#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import json
from Source_DB import QYT_Teachers,QYT_Courses #导入字典

# print(QYT_Teachers)#打印字典
# print(QYT_Courses)#打印字典

print('把Python对象转换为JSON格式，并且写入文件')
with open('JSON_0_QYT_Teachers.json', 'w', encoding='utf-8') as f:
    json.dump(QYT_Teachers, f, ensure_ascii=False)

with open('JSON_0_QYT_Courses.json', 'w', encoding='utf-8') as f:
    json.dump(QYT_Courses, f, ensure_ascii=False)


print('='*80)
print('可以使用json.dumps方法转换任何Python对象到字符串')
print('-'*80)
QYT_Teachers_JSON = json.dumps(QYT_Teachers,ensure_ascii=False)
print('其实\n'+QYT_Teachers_JSON+'\n是字符串')

print('='*80)
print('读取JSON文件，并且转换为Python对象')
print('-'*80)
with open('JSON_0_QYT_Teachers.json', 'r', encoding='utf-8') as f:
    QYT_Teachers_New = json.load(f)

with open('JSON_0_QYT_Courses.json', 'r', encoding='utf-8') as f:
    QYT_Courses_New = json.load(f)

#注意JSON中的小true问题
with open('JSON_0_JSON_true.json', 'r') as f:
    JSON_true = json.load(f)

#打印Python对象
print(QYT_Teachers_New)
print(QYT_Courses_New)
print(JSON_true)


print('='*80)
print('直接把字符串转换为Python对象')
print('-'*80)

#严重注意JSON内部必须为双引号
QYTANG_DICT_STR = '{"qytang":[1,2,3]}'
QYTANG_LIST_STR = "[1,2,3,4,5]"
#严重注意JSON的小true问题
QYTANG_JSON_true_STR = '{"qytang":true}'

QYTANG_DICT = json.loads(QYTANG_DICT_STR)
QYTANG_LIST = json.loads(QYTANG_LIST_STR)
QYTANG_JSON_true = json.loads(QYTANG_JSON_true_STR )

print(QYTANG_DICT)
print(type(QYTANG_DICT))
print(QYTANG_LIST)
print(type(QYTANG_LIST))
print(QYTANG_JSON_true)
print(type(QYTANG_JSON_true))