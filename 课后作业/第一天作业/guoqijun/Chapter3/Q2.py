x_rate = 0.65
total_dollars = 200
fee = 2

total_pounds = (int(total_dollars) - int(fee)) * float(x_rate)

total_dollars = (float(total_pounds) - int(100)) / float(x_rate) - int(fee)

print(int(total_dollars))
