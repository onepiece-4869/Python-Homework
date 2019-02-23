#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import ftplib
import os


def putfile(site, file, user=('anonymous', '1@2.net'), rdir='.', ldir='.', verbose=True):
    if verbose:  # 如果详细显示
        print('Uploading', file)  # 打印开始信息
    os.chdir(ldir)  # 切换本地目录
    local = open(file, 'rb')  # 打开本地文件
    remote = ftplib.FTP(site)  # 连接远程再点
    remote.encoding = 'GB18030'  # 编码方式
    remote.login(*user)  # 输入用户和密码
    remote.cwd(rdir)  # 切换FTP目录
    remote.storbinary('STOR ' + file, local, 1024)  # 上传文件
    remote.quit()  # 退出FTP
    local.close()  # 关闭本地打开文件
    if verbose:  # 如果详细显示
        print('Upload done.')  # 打印结束信息


if __name__ == '__main__':
    # 需要在CLI页面执行,PyCharm Python Console显示有问题
    import getpass
    ftphost = input('请输入FTP主机IP地址:')
    filename = input('请输入文件名:')
    username = input('请输入用户名:')
    password = getpass.getpass(prompt='请输入密码:')
    putfile(ftphost, filename, user=(username, password))
