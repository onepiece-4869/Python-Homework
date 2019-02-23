def five(num):
    num = 5
    num += 1
    return num

print(five(2))

def main(num):
    num = 1
    five(2)
    return num

print(main(2))