quantity_of_num = int(input("Укажите кол-во вводных данных: "))
if quantity_of_num < 2 :
    count_chek_quantity = 1
    while count_chek_quantity < 3 and quantity_of_num < 2 :
        print("Кол-во не меньше 2")
        quantity_of_num = int(input("Укажите кол-во вводных данных: "))
        count_chek_quantity += 1
if quantity_of_num > 1 :
    num = int(input("Введите число: "))
    count_of_enter = 1
    flag = False
    if count_of_enter == 1 :
        num_prev = num
        num = int(input("Введите число: "))
        count_of_enter += 1
    if quantity_of_num > 2 :
        difference = num - num_prev
        while not flag and count_of_enter < quantity_of_num :
            num_prev = num
            num = int(input("Введите число: "))
            if num - num_prev != difference :
                flag = True
            count_of_enter += 1
    if flag :
        print("Не является арифметической прогрессией")
    else :
        print("Арифметическая прогрессия")