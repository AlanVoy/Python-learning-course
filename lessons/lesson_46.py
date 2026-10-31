quantity_num = int(input("Укажите количество(не менее 2): "))
if quantity_num < 2 :
    check_quantity_num = 1
    while quantity_num < 2 and check_quantity_num < 3 :
        print("Количество не может быть меньше 2")
        quantity_num = int(input("Укажите количество(не менее 2): "))
        check_quantity_num += 1
else :
    count_enter = 0
    count_more_prev = 0
    while count_enter < quantity_num :
        if count_enter == 0 :
            num = int(input("Введите число: "))
            count_enter += 1
        else :
            num_prev = num
            num = int(input("Введите число: "))
            if num > num_prev :
                count_more_prev += 1
            count_enter += 1
    print("Чисел строго больше предыдущих:", count_more_prev)