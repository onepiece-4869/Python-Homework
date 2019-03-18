#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import sqlite3

homework_dict = [{'姓名': '学员1', '年龄': 37, '作业数': 1}, {'姓名': '学员2', '年龄': 33, '作业数': 5}, {'姓名': '学员3', '年龄': 32, '作业数': 10}]
connect = sqlite3.connect('qytang.db')
cursor = connect.cursor()

cursor.execute("create table qytang_homework_info (姓名 varchar(40), 年龄 int, 作业数 int)")

for student in homework_dict:
    name = student['姓名']
    age = student['年龄']
    homework = student['作业数']
    cursor.execute("insert into qytang_homework_info values ('%s', %d, %d)" % (name, age, homework))
connect.commit()

if __name__ == '__main__':
    pass

