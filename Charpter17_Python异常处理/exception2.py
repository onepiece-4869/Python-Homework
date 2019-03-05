#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

def find_index(obj, index):
    print(obj[index])

if __name__ == '__main__':
    import re
    try:
        find_index('qytang', 'cisco')
#    except:               #它会捕获所有异常，even system exitcalls and Ctrl-C key combinations
#        pass
    except Exception:     #推荐捕获除了system exitcalls and Ctrl-C key combinations以外的异常
        pass
#    except Exception as e: #打印异常内容
#        print(e)
    else:
        print('没有任何错误发生！')
    finally:
        print('这个总是要打印的！')