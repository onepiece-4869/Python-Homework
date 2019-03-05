department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

line1 ='Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f %s' % (department1,depart1_m,COURSE_FEES_SEC,'The End!')
line2 ='Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f %s' % (department2,depart2_m,COURSE_FEES_Python,'The End!')

# line1 ='Department1 name:{0:<10} Manager:{1:<10} COURSE FEES:{2:<10.2f} {3}'.format(department1,depart1_m,COURSE_FEES_SEC,'The End!')
# line2 ='Department2 name:{0:<10} Manager:{1:<10} COURSE FEES:{2:<10.2f} {3}'.format(department2,depart2_m,COURSE_FEES_Python,'The End!')

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)