#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import json
from dateutil import parser
from datetime import timedelta

#源字符串(有问题，需要排错)
test_str_source = "{'姓名': '秦柯', '年龄': 39, '出生日期': '1979-05-05', '状态': true}"
#修改后字符串
test_str_source = '{"姓名": "秦柯", "年龄": 39, "出生日期": "1979-05-05", "状态": true}'
#转换字符串到python字典
test_dict = json.loads(test_str_source)
print(test_dict)
#让我变成80后
test_dict['出生日期'] = (parser.parse(test_dict['出生日期']) + timedelta(days= 365 * 10)).strftime('%Y-%m-%d')
#打印字典（第二次打印）
print(test_dict)

#写入Python字典到JSON文件
test_str_json = json.dumps(test_dict,ensure_ascii=False)
#读取JSON文件并转换为字典
test_dict_read = json.loads(test_str_json)
#读取字典(第三次打印)
print(test_dict_read)