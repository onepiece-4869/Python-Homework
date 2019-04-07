#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import paramiko
import re


def qytang_ssh(ip, username, password, cmd='show run', port=22):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip, username=username, password=password, port=port, timeout=5, compress=True)
        stdin, stdout, srderr = ssh.exec_command(cmd)
        x = stdout.read().decode()
        if re.findall('Line has invalid autocommand', x):
            print('命令不能被执行!请检查用户权限!')
        else:
            return x


    except paramiko.AuthenticationException as e:
        print('认证错误', e)
    except Exception as e:
        # print(e)
        if re.findall('timed out', str(e)):
            print('连接超时', 'timed out')
        elif re.findall('Unable to connect to port 22 on 192.168.11.120', str(e)):
            print('SSH请求被管理过滤', e)



if __name__ == '__main__':
    print(qytang_ssh('192.168.11.120', 'admin', 'cisco'))


