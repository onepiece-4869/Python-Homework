#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import base64

def bytes_b64(convert_bytes):
    bytes_b64code = base64.b64encode(convert_bytes)
    bytes_b64code = str(bytes_b64code)[2:-1]
    return bytes_b64code

def b64_bytes(b64):
    b4code_back = bytes(b64, 'utf8')
    signature = base64.b64decode(b4code_back)
    return signature

if __name__ == '__main__':
    test_bytes = b'\xac!{'
    base64_result = bytes_b64(test_bytes)
    print(base64_result)
    bytes_result = b64_bytes(base64_result)
    print(bytes_result)
