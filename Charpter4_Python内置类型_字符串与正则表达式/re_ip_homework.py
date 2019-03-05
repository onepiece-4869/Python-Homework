import re

str1 = 'Port-channel1.189          192.168.189.254  YES     CONFIG   up                       up '
result = re.match('\s*(\w.*\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w*)\s*',str1).groups()
print(result)

print('-'*80)
print('%-8s %2s %s' % ('接口',':',result[0]))
print('%-8s %2s %s' % ('IP地址',':',result[1]))
print('%-8s %2s %s' % ('接口状态',':',result[-1]))