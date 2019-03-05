department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'

COURSE_FEES_Security = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = 'Department Name:%-10s Manager:%-10s COURSE FEE:%-10.2f THE END!' % (department1,depart1_m,COURSE_FEES_Security)
line2 = 'Department Name:%-10s Manager:%-10s COURSE FEE:%-10.2f THE END!' % (department2,depart2_m,COURSE_FEES_Python)

length = len(line1)

print('='*length)
print(line1)
print(line2)
print('='*length)

