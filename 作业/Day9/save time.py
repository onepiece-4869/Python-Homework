#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import paramiko

datetime_now = datetime.datetime.now()
fivedaysago = datetime_now - datetime.timedelta(5)
othertimeformat = datetime_now.strftime('%Y-%m-%d_%H-%M-%S')
file_name = 'save_fivedayago_time_{0}'.format(othertimeformat)
time_file = open(file_name, 'w')
time_file.write(str(fivedaysago))
time_file.close()

if __name__ == '__main__':
    pass

