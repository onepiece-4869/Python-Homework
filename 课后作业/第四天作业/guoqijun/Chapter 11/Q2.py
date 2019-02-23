def five():
    global num
    num =+ 1
    return num

five()

print(num)

def main():
    global num
    num = 1
    return num

main()

print(num)