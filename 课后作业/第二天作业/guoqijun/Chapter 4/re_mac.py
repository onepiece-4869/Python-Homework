str1 = '166  54a2.74f7.0326   DYNAMIC  Gi1/0/11'

import re

result = re.match('(\d+)\s+(\w{4}\.\w{4}\.\w{4})\s+([A-Z]+)\s+(\w+\d\/\d\/\d+)',str1).groups()

print('-'*80)
print('%-10s : %s' % ('VLAN ID',result[0]))
print('%-10s : %s' % ('MAC ADD',result[1]))
print('%-10s : %s' % ('Type',result[2]))
print('%-10s : %s' % ('Interface',result[3]))