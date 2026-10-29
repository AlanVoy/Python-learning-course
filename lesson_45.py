quantity_num = int(input("Укажите количество чисел(не менее 3): "))
if quantity_num < 3 :
    count_enter_quantity = 1
    while count_enter_quantity < 3 and quantity_num < 3 :
        print("Количество не менее 3 !")
        quantity_num = int(input("Укажите количество чисел(не менее 3): "))
        count_enter_quantity += 1
else :
    count_local_maximum = 0
    count_enter_num = 0
    while count_enter_num < quantity_num :
        if count_enter_num == 0 :
            num_prev = int(input("Введите число: "))
            count_enter_num += 1
        elif count_enter_num == 1 :
            num = int(input("Введите число: "))
            count_enter_num += 1
        elif count_enter_num == 2 :
            num_post = int(input("Введите число: "))
            if num_prev < num > num_post :
                count_local_maximum += 1
            count_enter_num += 1
        else :
            num_prev = num
            num = num_post
            num_post = int(input("Введите число: "))
            if num_prev < num > num_post :
                count_local_maximum += 1
            count_enter_num += 1
    print("Количество локальных максимумов:",count_local_maximum)