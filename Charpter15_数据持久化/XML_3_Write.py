#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from xml.dom.minidom import Document

doc = Document()
root = doc.createElement('root')
doc.appendChild(root)  # 创建根

QYT_Company = doc.createElement('公司')
QYT_Company.setAttribute('name', '亁颐堂')

root.appendChild(QYT_Company)  # 在根下创建公司
#############################################
Department = doc.createElement('部门')
Department.setAttribute('name', '安全')

QYT_Company.appendChild(Department)  # 在公司下创建安全部门

QYT_Description = doc.createElement('部门简介')
Department.appendChild(QYT_Description)  # 在部门下创建部门简介

QYT_Description_Text = doc.createTextNode('\n\t\t\t\t主要从事思科安全产品与课程研发\n\t\t\t')
QYT_Description.appendChild(QYT_Description_Text)  # 创建部门简介的文本TEXT

Teachers = doc.createElement('师资')
Teachers.setAttribute('name', '安全团队')
Department.appendChild(Teachers)  # 在部门下创建师资

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '秦柯')
Teachers.appendChild(Teacher_Name)  # 在师资下创建老师‘秦柯’

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '李冰')
Teachers.appendChild(Teacher_Name)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '刘强龙')
Teachers.appendChild(Teacher_Name)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '杨金超')
Teachers.appendChild(Teacher_Name)

Kecheng = doc.createElement('课程')
Kecheng.setAttribute('name', 'Security CCNP')
Department.appendChild(Kecheng)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'CCNASec')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'ACS5')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'Firewall')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'VPN')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'ISE')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'IPS')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'Secure')
Kecheng.appendChild(Kecheng_Name)

#############################################
Department = doc.createElement('部门')
Department.setAttribute('name', '无线')

QYT_Company.appendChild(Department)

QYT_Description = doc.createElement('部门简介')
Department.appendChild(QYT_Description)

QYT_Description_Text = doc.createTextNode('\n\t\t\t\t主要从事思科无线产品与课程研发\n\t\t\t')
QYT_Description.appendChild(QYT_Description_Text)

Teachers = doc.createElement('师资')
Teachers.setAttribute('name', '无线团队')
Department.appendChild(Teachers)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '秦柯')
Teachers.appendChild(Teacher_Name)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '刘强龙')
Teachers.appendChild(Teacher_Name)

Kecheng = doc.createElement('课程')
Kecheng.setAttribute('name', 'Wireless CCNP')
Department.appendChild(Kecheng)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', '无线控制器')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'ISE')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'PI_MSE')
Kecheng.appendChild(Kecheng_Name)

#############################################
Department = doc.createElement('部门')
Department.setAttribute('name', '数据中心')

QYT_Company.appendChild(Department)

QYT_Description = doc.createElement('部门简介')
Department.appendChild(QYT_Description)

QYT_Description_Text = doc.createTextNode('\n\t\t\t\t主要从事思科数据中心产品与课程研发\n\t\t\t')
QYT_Description.appendChild(QYT_Description_Text)

Teachers = doc.createElement('师资')
Teachers.setAttribute('name', '数据中心团队')
Department.appendChild(Teachers)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '马海波')
Teachers.appendChild(Teacher_Name)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '姜帆')
Teachers.appendChild(Teacher_Name)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', '秦柯')
Teachers.appendChild(Teacher_Name)

Kecheng = doc.createElement('课程')
Kecheng.setAttribute('name', 'DataCenter CCNP')
Department.appendChild(Kecheng)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'Nexus交换机')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', '数据存储')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', 'UCS')
Kecheng.appendChild(Kecheng_Name)

#############################################
Department = doc.createElement('部门')
Department.setAttribute('name', '路由交换')

QYT_Company.appendChild(Department)

QYT_Description = doc.createElement('部门简介')
Department.appendChild(QYT_Description)

QYT_Description_Text = doc.createTextNode('\n\t\t\t\t主要从事思科路由交换产品与课程研发\n\t\t\t')
QYT_Description.appendChild(QYT_Description_Text)

Teachers = doc.createElement('师资')
Teachers.setAttribute('name', '路由交换团队')
Department.appendChild(Teachers)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', "周亚军")
Teachers.appendChild(Teacher_Name)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', "李伟达")
Teachers.appendChild(Teacher_Name)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', "白伟鹏")
Teachers.appendChild(Teacher_Name)

Teacher_Name = doc.createElement('老师')
Teacher_Name.setAttribute('name', "杨学宝")
Teachers.appendChild(Teacher_Name)

Kecheng = doc.createElement('课程')
Kecheng.setAttribute('name', 'RS CCNP')
Department.appendChild(Kecheng)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', '路由')
Kecheng.appendChild(Kecheng_Name)

Kecheng_Name = doc.createElement('课程名')
Kecheng_Name.setAttribute('name', '交换')
Kecheng.appendChild(Kecheng_Name)

XML_File = open('XML_4_Write.xml', 'w', encoding='utf-8')
XML_File.write(doc.toprettyxml(indent='    '))
XML_File.close()
