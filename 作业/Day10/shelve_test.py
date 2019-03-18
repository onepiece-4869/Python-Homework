#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import shelve
import datetime

db = shelve.open('date_shelve')
db['savetime'] = datetime.date.today()
db.close()
db = shelve.open('date_shelve')
db['savetime'] = datetime.datetime.now()
db.close()
db = shelve.open('date_shelve')
db_read = db['savetime']
othertimeformat = db_read.strftime('%Y-%m-%d %H::%M::%S')
print(othertimeformat)

if __name__ == '__main__':
    pass

