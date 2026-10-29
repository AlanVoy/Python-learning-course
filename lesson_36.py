num = int(input("Кол-во чисел для вывода: "))
if num > 0 :
    if num > 0 and num < 3 :
        num_str = str()
        count = num
        num_n = 0
        while count > 0 :
            num_str = num_str + str(num_n)
            num_n += 1
            count -= 1
        print(num_str)
    elif num > 2 :
        num_str = str("0,1")
        count = num - 2
        num_1 = 0
        num_2 = 1
        num_save = int()
        while count > 0 :
            num_save = num_1
            num_1 = num_2
            num_2 = num_save + num_1
            num_str = num_str + "," + str(num_2)
            count -= 1
        print(num_str)
else :
    print("Ошибка ввода")