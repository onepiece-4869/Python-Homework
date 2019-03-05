import sys

if 'win' in sys.platform:
    print('this is windows!')
elif 'linux' in sys.platform:
    print('this is liunx!')
else:
    print('other system')