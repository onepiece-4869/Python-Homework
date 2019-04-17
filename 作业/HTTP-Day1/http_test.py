#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import requests

r = requests.get('http://192.168.11.100:8000/monitor_device/line/1/')

print(r.json())
print('时间:', r.json().get('labels'))
print('数据:', r.json().get('datas'))
print(type(r.json()))



