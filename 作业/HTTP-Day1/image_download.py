#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import requests
from PIL import Image
from io import BytesIO


def get_header_dict(txtfile):
    header_dict = {}
    headers_txt = open(txtfile)
    for x in headers_txt.readlines():
        header_line = x.strip().split(':')
        header_dict[header_line[0].strip()] = header_line[1].strip()
    return header_dict


# imgContent = r.content
#
# i = Image.open(BytesIO(r.content))
# i.show()


if __name__ == '__main__':
    r = requests.get('http://192.168.11.100:8000/static/images/logo_long_new.png', headers=get_header_dict('headers.txt'), verify=False)
    imgContent = r.content
    i = Image.open(BytesIO(r.content))
    i.show()

    imageFile = open('2_response_3_image.jpg', 'wb')
    imageFile.write(imgContent)
    imageFile.close()


