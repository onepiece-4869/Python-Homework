import os

os.popen('route print').read()

result = os.popen('route print').read().split('\n')

str = result[16].split(' ')

if str[10] == str[20] == '0.0.0.0':
    print('网关为:' + str[24])
