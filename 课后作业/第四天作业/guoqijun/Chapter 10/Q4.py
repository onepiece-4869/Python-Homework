import os
import time

while True:
    result = os.popen('netstat -tulnp').read()
    result_list = result.split('\n')
    result_list = result_list[2:-1]
    for x in result_list:
        if x.split()[3].split(':')[-1] == '80':
            print('HTTP (TCP/80) has been opened')
            break
    else:
         print('Wait one second to restart monitoring!')
         time.sleep(1)
         continue
    break