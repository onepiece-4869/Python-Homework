#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import poplib
import re
import email
import base64
import time
from Tools.paramiko_ssh import qytang_ssh
from Tools.send_mail import qyt_smtp_attachment


def decode_subject_base64(str):
    try:
        re_result = re.match('=\?(.*)\?\w\?(.*)\?=', str).groups()
        middle = re_result[1]
        decoded = base64.b64encode(middle)
        decoded_str = decoded.decode(re_result[0])
    except Exception as e:
        decoded_str = str
    return decoded_str


def qyt_rec_mail(mailserver, mailuser, mailpasswd, save_file=False, delete_email=False):
    print('Connecting...')
    server = poplib.POP3_SSL(mailserver, 995)
    server.user(mailuser)
    server.pass_(mailpasswd)
    mails_list = []
    try:
        print(server.getwelcome())
        msgCount, msgBytes = server.stat()
        print('There are', msgCount, 'mail message in', msgBytes, 'bytes')
        # print(server.list())

        for i in range(msgCount):
            hdr, message, octets = server.retr(i + 1)
            str_message = email.message_from_bytes(b'\n'.join(message))
            part_list = []
            mail_dict = {}
            for part in str_message.walk():
                part_list.append(part)
            # print(part_list[0].items())

            for header_name, header_content in part_list[0].items():
                if header_name == 'From':
                    # print(decode_subject_base64(header_content))
                    mail_dict[header_name] = decode_subject_base64(header_content)
                    # print(len(mail_dict[header_name]))
                else:
                    mail_dict[header_name] = header_content

                if header_name == 'Subject':
                    mail_dict[header_name] = decode_subject_base64(header_content)
                else:
                    mail_dict[header_name] = header_content
            # print(type(mail_dict['From']))
            if not re.match('".*" (<726128572@qq.com>)', mail_dict['From']):
                print('发件人不正确!无法执行命令!')
                break

            mail_dict['Attachment'] = []
            mail_dict['Images'] = []

            if len(part_list) > 1:
                for i in range(1, len(part_list)):

                    content_charset = part_list[i].get_content_charset()
                    content_type = part_list[i].get_content_type()
                    print(part_list[i].items())

                    if content_type == 'application/octet-stream':
                        attach = mail_dict.get('Attachment')
                        attach_filename = part_list[i].get_filename()
                        attach_file_bit = base64.b64encode(part_list[i].get_payload())
                        attach.append((attach_filename, attach_file_bit))
                        mail_dict['Attachment'] = attach

                        if save_file:
                            fp = open(attach_filename, 'wb')
                            fp.write(attach_file_bit)
                            fp.close()
                    elif 'text' in content_type:
                        try:
                            decoded = base64.b16decode(part_list[i].get_payload())
                            decoded_str = decoded.decode(content_charset)
                            mail_dict['Body'] = decoded_str
                        except Exception as e:
                            mail_dict['Body'] = part_list[i].get_payload()
                    elif 'image' in content_type:
                        images = mail_dict.get('Images')
                        image_name = part_list[i].get('Content-ID') + '.' + content_type.spilt('/')[1]
                        image_bit = base64.b16decode(part_list[i].get_payload())
                        images.append((image_name, image_bit))
                        mail_dict['Images'] = images

                        if save_file:
                            fp = open(image_name, 'wb')
                            fp.write(image_bit)
                            fp.close()
            mails_list.append(mail_dict)
        if delete_email:
            for msg_id in range(msgCount):
                server.dele(msg_id + 1)
    finally:
        server.quit()

    return mails_list


if __name__ == '__main__':
    while True:
        mail_lists = qyt_rec_mail('pop.qq.com', '3348326959@qq.com', 'dmyymagcazklcjie', save_file=True, delete_email=True)
        # i = 1
        if mail_lists:
            for x in mail_lists:
                # print('=' * 50, '第', i, '封信', '=' * 50)
                for key, value in x.items():
                    # print(key, '==>', value)
                    if key == 'Subject':
                        cmd = re.match('cmd:(\w+)', value.strip()).groups()[0]
                        print(cmd)
                        mail_subject = 'cmd {0} exec result'.format(cmd)
                        Main_Body = qytang_ssh('192.168.11.100', 'root', 'python', cmd=cmd)

                        qyt_smtp_attachment('smtp.qq.com',
                                            '3348326959@qq.com',
                                            'dmyymagcazklcjie',
                                            '3348326959@qq.com',
                                            '726128572@qq.com;xiaoyang429670@gmail.com',
                                            mail_subject,
                                            Main_Body)
                # i += 1
        else:
            print('暂无需要执行的任务!')
        time.sleep(60)

