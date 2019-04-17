#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth


r = requests.get('http://192.168.11.120/level/15/exec/-/show/ip/interface/brief/CR', auth=HTTPBasicAuth('admin', 'cisco'))
print(r.text)
