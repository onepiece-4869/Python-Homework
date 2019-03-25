#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import paramiko


def qytang_ssh(ip, username, password, cmd='ls', port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip, username=username, password=password, port=port, timeout=5, compress=True)
    stdin, stdout, srderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(qytang_ssh('192.168.121.100', 'root', 'python'))
    print(qytang_ssh('192.168.121.100', 'root', 'python', cmd='pwd'))


