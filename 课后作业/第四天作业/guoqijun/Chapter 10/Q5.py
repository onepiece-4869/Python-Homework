list1 = ['aaa',111,(4,5),2.01]
list2 = ['bbb',333,111,3.14,(4,5)]

same_object = []

for x in list1:
    if x in list2:
        same_object.append(x)

print(same_object)