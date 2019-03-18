#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import pickle
import datetime
import os

file_name = '{0}.pl'.format(datetime.date.today())
a = {'today': datetime.date.today()}
db = open(file_name, 'wb')
pickle.dump(a, db)
db.close()
db_file = open(file_name, 'rb')
db_read = pickle.load(db_file)
db_file.close()
db_read['today'] += datetime.timedelta(5)
db_file = open(file_name, 'wb')
pickle.dump(db_read, db_file)
db_file.close()
new_time = datetime.date.today() + datetime.timedelta(5)
file_name_new = '{0}.pl'.format(new_time)
os.rename(file_name, file_name_new)
db_file = open(file_name_new, 'rb')
db_read = pickle.load(db_file)
db_file.close()
print('today', '=>', db_read['today'])
os.remove(file_name_new)

if __name__ == '__main__':
    pass
