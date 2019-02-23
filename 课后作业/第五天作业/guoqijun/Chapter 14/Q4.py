import datetime

now = datetime.datetime.now()

fivedayago = (datetime.datetime.now() - datetime.timedelta(days = 5))

otherstyletime = now.strftime('%Y-%m-%d_%H-%M-%S')

time_file_name = 'save_fivedayago_time_' + otherstyletime + '.txt'

time_file = open(time_file_name,'w')

time_file.write(str(fivedayago))