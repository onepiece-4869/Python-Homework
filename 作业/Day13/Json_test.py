#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import json
from datetime import timedelta
from dateutil import parser

test_str_source = "{'姓名': '秦柯', '年龄': 39, '出生日期': '1979-05-05', '状态': true}"

test_str_source = '{"姓名": "秦柯", "年龄": 39, "出生日期": "1979-05-05", "状态": true}'

test_dict = json.loads(test_str_source)

print(test_dict)

test_dict['出生日期'] = (parser.parse(test_dict['出生日期']) + timedelta(days=365 * 10)).strftime('%Y-%m-%d')

test_str_json = json.dumps(test_dict, ensure_ascii=False)

test_dict_read = json.loads(test_str_json)

print(test_dict_read)

if __name__ == '__main__':
    pass

