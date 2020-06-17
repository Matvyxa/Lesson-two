my_list = ["Имя", 34, 4.2, True, None]
for i in range(len(my_list)):
    if i > 0:
        my_list[0], my_list[1] = my_list[1], my_list[0]
        my_list[2], my_list[3] = my_list[3], my_list[2]
        i = i + 1
    else:
        my_list[-1] = my_list[-1]
    print(my_list)