#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from xml.dom.minidom import Document
from Source_DB import QYT_Teachers, QYT_Courses, kecheng_dict  # 导入字典

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)

QYT_Company = doc.createElement('公司')
QYT_Company.setAttribute('name', '亁颐堂')

root.appendChild(QYT_Company)
#############################################
for Department in QYT_Teachers:
    Depart = doc.createElement('部门')
    Depart.setAttribute('name', Department)
    QYT_Company.appendChild(Depart)

    QYT_Description = doc.createElement('部门简介')
    Depart.appendChild(QYT_Description)

    QYT_Description_Text = doc.createTextNode('\n\t\t\t\t主要从事思科%s产品与课程研发\n\t\t\t' % Department)
    QYT_Description.appendChild(QYT_Description_Text)

    Teachers = doc.createElement('师资')
    Teachers.setAttribute('name', '%s团队' % Department)
    Depart.appendChild(Teachers)

    for Teacher in QYT_Teachers[Department]:
        Teacher_Name = doc.createElement('老师')
        Teacher_Name.setAttribute('name', Teacher)
        Teachers.appendChild(Teacher_Name)

    Kecheng = doc.createElement('课程')
    Kecheng.setAttribute('name', kecheng_dict[Department])
    Depart.appendChild(Kecheng)

    for Course in QYT_Courses[Department]:
        Kecheng_Name = doc.createElement('课程名')
        Kecheng_Name.setAttribute('name', Course)
        Kecheng.appendChild(Kecheng_Name)

XML_File = open('XML_6_Auto_Write.xml', 'w',  encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()
