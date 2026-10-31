quantity_num = int(input("Укажите количество(не менее 2): "))
if quantity_num < 2 :
    count_quantity = 1
    while count_quantity < 3 and quantity_num < 2:
        print("Количество не менее 2")
        quantity_num = int(input("Укажите количество(не менее 2): "))
        count_quantity += 1
    if count_quantity == 3 and quantity_num < 2:
        print("Неверный ввод. Завершение программы")
if quantity_num > 1 :
    count_series = 0
    count_enter = 0
    while count_enter < quantity_num :
        if count_enter == 0 :
            num = int(input("Введите число: "))
            count_enter += 1
            count_series += 1
        else :
            prev_num = num
            num = int(input("Введите число: "))
            if prev_num != num :
                count_series += 1
            count_enter += 1
    print("количество серий: ", count_series)